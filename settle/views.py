# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from settle.steam_news import get_news
from settle.models import Post, Comment, Tag, User
from settle.forms import SignupForm, CommentForm, UploadForm, SuggestTag, AddFavGame
from django import forms
from django.utils import timezone
from settle.validators import CPasswordValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.


def redirectHome(request):
    response = redirect('/settle')
    return response


def index(request, template="settle/index.html", valid=None):
    context_dict = {}
    context_dict['valid'] = valid

    post_list = Post.objects.all().order_by("-date_submitted")
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context_dict['posts'] = posts
    return render(request, 'settle/index.html', context_dict)

def handler404(request):
    return render(request, 'settle/404.html', status=404)

def handler500(request):
    return render(request, 'settle/500.html', status=500)

@login_required
def feed(request):
    context_dict = {}

    # need to filter this for feed
    fav_games = list(request.user.favourite_games.all())
    post_list = Post.objects.all().filter(game_tag__in=fav_games)
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'settle/feed.html', {'posts': posts})


@login_required
def upload(request):
    context_dict = {}

    game_tags = Tag.objects.filter(is_game_tag=True).filter(
        is_pending=False).order_by("text")
    info_tags = Tag.objects.filter(is_game_tag=False).filter(
        is_pending=False).order_by("text")

    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            user_post = upload_form.save(commit=False)
            user_post.author = request.user

            if 'picture' in request.FILES:
                user_post.picture = request.FILES['picture']

            user_post.save()
            upload_form.save_m2m()

        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()

    context_dict["game_tags"] = game_tags
    context_dict["info_tags"] = info_tags
    context_dict["upload_form"] = upload_form

    return render(request, 'settle/upload.html', context=context_dict)


@login_required
def post(request, post_id):
    context_dict = {}
    result_list = []

    post = Post.objects.filter(id=post_id)[0]
    context_dict['form'] = CommentForm()

    if request.method == 'POST':
        # Check the type of post request
        if request.POST.get('type') == "com":
            # Use the CommentForm
            comment_form = CommentForm(data=request.POST)
            context_dict['form'] = comment_form

            # Check the data given is valid
            if comment_form.is_valid():
                # Get the user from the request data
                newComment = comment_form.save(commit=False)
                # Get the user that submitted the comment
                un = request.POST.get('author')
                # Set the author and the parent post
                newComment.author = User.objects.get(username=un)
                newComment.parent_post = Post.objects.filter(id=post_id)[0]

                # Save the comment
                comment_form.save()
            else:
                # Print the errors from the form
                print(comment_form.errors)
        # If a like request, update the comment
        elif request.POST.get('type') == "like":
            # Get the id of the comment and get the comment object
            c = request.POST.get('comment')
            comment = Comment.objects.get(id=c)
            # Get the user id and find the user object
            un = request.POST.get('liker')
            liker = User.objects.get(username=un)

            # If the user hasn't liked the comment, like it, else unlike it
            if liker not in comment.liking_users.all():
                comment.liking_users.add(liker)
            else:
                comment.liking_users.remove(liker)
        elif request.POST.get('type') == "del":
            c = request.POST.get('comment')
            Comment.objects.filter(id=c).delete()

    else:
        # Give it back an empty form
        context_dict['form'] = CommentForm()

    all_comments = Comment.objects.filter(parent_post=post_id).annotate(
        num_likes=Count('liking_users')).order_by('-num_likes')
    comment_count = len(all_comments)

    comm_pagin = Paginator(all_comments, 3)  # show 3 comments at once

    # get page no. from URL, or 1 if just loading in
    page = request.GET.get('page', 1)

    try:
        comments = comm_pagin.page(page)  # get the given page of comments
    except PageNotAnInteger:
        comments = comm_pagin.page(1)  # default to 1st page if not a number
    except EmptyPage:
        # default to last page if too big
        comments = comm_pagin.page(comm_pagin.num_pages)

    app_id = post.game_tag.steamAppId

    if app_id != 0:
        result_list = get_news(app_id, 10)
    # result_list = get_news(440, 5)
    context_dict["result_list"] = result_list
    context_dict["post"] = post
    context_dict["comments"] = comments
    context_dict["comment_count"] = comment_count

    return render(request, 'settle/post.html', context=context_dict)


def signup(request):
    # Used to tell us if signup was successful
    registered = False

    if request.method == 'POST':
        # Use the signup_form
        signup_form = SignupForm(data=request.POST)

        # Check the data given is valid
        if signup_form.is_valid():
            # Get the user from the form
            newUser = signup_form.save(commit=False)
            # Get the cleaned data
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password']
            # Make a new valdator from our custom class
            pwValidator = CPasswordValidator()
            try:
                # Check the password is valid
                pwValidator.validate(password, newUser)
            except ValidationError as e:
                # Else add the errors to the form
                signup_form.add_error('password', e)
                # Return the falied form
                return render(request, 'settle/register.html', {'form': signup_form, 'registered': registered})
            # Save the new user
            newUser.password = make_password(password, hasher="pbkdf2_sha256")
            newUser.save()

            registered = True
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirectHome(request)
        else:
            # Print the errors from the form
            print(signup_form.errors)
    else:
        # Give it back an empty form
        signup_form = SignupForm()

    return render(request, 'settle/register.html', {'form': signup_form, 'registered': registered})


def user_login(request):
    # If request is post, pull out relevent data
    valid = False
    if request.method == 'POST':
        # Get username and password from the post data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if it is a valid user
        user = authenticate(username=username, password=password)

        # If a valid user
        if user:
            login(request, user)
            return redirectHome(request)
        else:
            return index(request, valid=valid)
    else:
        return index(request)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def suggest_tag(request):
    context_dict = {}

    if request.method == "POST":
        if request.POST.get('type') == 'suggest':
            suggest_tags_form = SuggestTag(request.POST)

            if suggest_tags_form.is_valid():
                new_tag = suggest_tags_form.save(commit=False)
                new_tag.is_pending = True
                u = request.POST.get('user')
                user = User.objects.get(username=u)

                if user.groups.filter(name='admin').exists():
                    new_tag.is_pending = False

                # Check if admin etc
                new_tag.save()
            else:
                print(suggest_tags_form.errors)
        elif request.POST.get('type') == 'del':
            t = request.POST.get('tag')
            Tag.objects.filter(id=t).delete()
            suggest_tags_form = SuggestTag()

    else:
        suggest_tags_form = SuggestTag()
    context_dict["suggest_form"] = suggest_tags_form

    pending_tags = Tag.objects.filter(is_pending=True).order_by("text")

    context_dict["pending_tags"] = pending_tags

    return render(request, 'settle/suggest-tag.html', context=context_dict)


@login_required
def account(request):
    context_dict = {}
    # Return the AddFavGame form
    context_dict['form'] = AddFavGame()
    # If a post request
    if request.method == "POST":
        # Get the type of post request
        code = request.POST.get('type')
        if code == "append":
            # Get the form with the data
            form = AddFavGame(request.POST)
            # Get the selected tags
            tagsSelected = request.POST.getlist('game_tags')
            # Get the user object
            u = request.POST.get('user')
            user = User.objects.get(username=u)

            # For each tag, add it to the fab games list for the user
            for tag in tagsSelected:
                tag = Tag.objects.get(id=tag)
                user.favourite_games.add(tag)
                user.save()
            # Return the filled form
            context_dict['form'] = form
        elif code == "delete":
            # Get the tag the user wants to remove
            t = request.POST.get('tag')
            tagToRemove = Tag.objects.get(id=t)
            u = request.POST.get('user')
            user = User.objects.get(username=u)
            # Remove the tag
            user.favourite_games.remove(t)
            user.save()

    return render(request, 'settle/account.html', context=context_dict)