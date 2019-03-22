# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.db.models import Count
from settle.steam_news import get_news
from settle.models import Post, Comment, Tag, User
from settle.forms import SignupForm, CommentForm, UploadForm, SuggestTag
from django import forms
from django.utils import timezone
from settle.validators import CPasswordValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.


def redirectHome(request):
    ''' Redirect to the index page.'''
    response = redirect('/settle')
    return response


def index(request, template="settle/index.html", valid=None):
    ''' Index view. '''
    context_dict = {}
    # Used to display any issues when trying to login
    context_dict['valid'] = valid

    # List of post we will display
    post_list = Post.objects.all().order_by("-date_submitted")
    page = request.GET.get('page', 1)

    # This is used for infinite scrolling
    paginator = Paginator(post_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Store the posts in the cd
    context_dict['posts'] = posts

    return render(request, 'settle/index.html', context_dict)


@login_required
def feed(request):
    ''' Feed view function.'''
    context_dict = {}

    # Get the game tags that users wish to see
    fav_games = list(request.user.favourite_games.all())
    # Get the posts we will display but only if they match the fav games tag
    post_list = Post.objects.all().filter(game_tag__in=fav_games).order_by("-date_submitted")

    # Used for infinte scrolling
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'settle/feed.html', {'posts': posts})


@login_required
def upload(request):
    ''' View used to upload an image to the page. '''
    context_dict = {}

    # Get all the info and game tags to send back to page
    game_tags = Tag.objects.filter(is_game_tag=True).filter(
        is_pending=False).order_by("text")
    info_tags = Tag.objects.filter(is_game_tag=False).filter(
        is_pending=False).order_by("text")

    # Check if the user has submitted an upload
    if request.method == "POST":
        # Use the upload form to store most of the data
        upload_form = UploadForm(request.POST, request.FILES)
        # Get the game tag from the request.POST
        game_tag = Tag.objects.filter(is_game_tag=True).filter(
            text=request.POST.get("game_tags"))

        user_info_tags = []
        # Find all the info tags the user has selected
        for tag in request.POST.getlist("info_tag_list"):
            user_info_tags.append(Tag.objects.get(text=tag))

        # If they have selected more than 5 inof tags, add a new error
        if len(user_info_tags) > 5:
            upload_form.add_error(
                'info_tags', 'Please select only up to 5 info tags.')
        else:
            if upload_form.is_valid():
                # Save the form and add the author and game tag
                user_post = upload_form.save(commit=False)
                user_post.author = request.user
                user_post.game_tag = game_tag[0]
                user_post.save()

                # Add the info tags to the post
                user_post.info_tags.set(user_info_tags)
                user_post.save()

                upload_form.cleaned_data["info_tags"] = user_post.info_tags.all()

                # Put the picture in the post
                if 'picture' in request.FILES:
                    user_post.picture = request.FILES['picture']

                # Save the post and it's m2m relationship
                user_post.save()
                upload_form.save_m2m()
                context_dict["message"] = "Success"
            else:
                print(upload_form.errors)

    else:
        # Give it an empty form to render
        upload_form = UploadForm()

    context_dict["game_tags"] = game_tags
    context_dict["info_tags"] = info_tags
    context_dict["upload_form"] = upload_form

    return render(request, 'settle/upload.html', context=context_dict)


def post(request, post_id):
    context_dict = {}
    result_list = []

    # get the post from post id passed
    post = Post.objects.filter(id=post_id)[0]
    context_dict['form'] = CommentForm()

    # for checking if a form was sent from the like/comment page
    context_dict["liked"] = False

    if request.method == 'POST':
        # Check the type of post request
        if request.POST.get('type') == "com":
            context_dict["liked"] = True
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
            context_dict["liked"] = True
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

        # for deleting a button
        elif request.POST.get('type') == "del":
            c = request.POST.get('comment')
            Comment.objects.filter(id=c).delete()

        # for deleting a post
        elif request.POST.get('type') == "post_del":
            p = request.POST.get('post')
            Post.objects.filter(id=p).delete()
            return redirectHome(request)

    else:
        # Give it back an empty form
        context_dict['form'] = CommentForm()

    # Get all the comments for the post
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

    # for getting news from the Steam API
    app_id = post.game_tag.steamAppId
    if app_id != 0:
        result_list = get_news(app_id, 5)

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
                return render(request, 'settle/register.html', {'signup_form': signup_form, 'registered': registered})
            # take the password entered by the user and hash it
            newUser.password = make_password(password, hasher="pbkdf2_sha256")
            # Save the new user
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

    return render(request, 'settle/register.html', {'signup_form': signup_form, 'registered': registered})


def user_login(request):
    # If request is post, pull out relevent data
    valid = False
    if request.method == 'POST':
        # Get username and password from the post data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if it is a valid user
        user = authenticate(username=username, password=password)

        # If a valid user login and redirect to home
        if user:
            login(request, user)
            return redirectHome(request)
        else:
            return index(request, valid=valid)
    else:
        return index(request)


@login_required
def user_logout(request):
    # logout and redirect to home
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def suggest_tag(request):
    context_dict = {}
    suggest_tags_form = SuggestTag()

    if request.method == "POST":
        # Check the type of post
        if request.POST.get('type') in ['suggest', 'approve']:

            if request.POST.get('type') == 'approve':
                # Delete the old tag as we will add the approved one
                text = request.POST.get('text')

                if Tag.objects.filter(text=text).exists():
                    t = Tag.objects.filter(text=text).delete()

            # Use suggest tag form
            suggest_tags_form = SuggestTag(request.POST)

            if suggest_tags_form.is_valid():
                # Make new tag, get the author
                new_tag = suggest_tags_form.save(commit=False)
                new_tag.is_pending = True

                if "is_game_tag" in request.POST:
                    new_tag.is_game_tag = True
                else:
                    # info tags shouldn't have a steam app id
                    new_tag.is_game_tag = False
                    new_tag.steamAppId = 0
                u = request.POST.get('user')
                user = User.objects.get(username=u)

                # If admin, don't make it pending
                if user.groups.filter(name='admin').exists():
                    new_tag.is_pending = False

                # Check if admin etc
                new_tag.save()
            else:
                print(suggest_tags_form.errors)
        # Delete the tag suggestion
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
    # If a post request
    if request.method == "POST":
        # Get the type of post request
        code = request.POST.get('type')
        if code == "append":
            # Get the list of tags the user wants to agg
            new_tags = []
            for tag in request.POST.getlist("fav_games"):
                new_tags.append(Tag.objects.get(text=tag))

            # Get the user object
            u = request.POST.get('user')
            user = User.objects.get(username=u)

            # For each tag, add it to the fab games list for the user
            for tag in new_tags:
                user.favourite_games.add(tag)
                user.save()

        elif code == "delete":
            # Get the tag the user wants to remove
            t = request.POST.get('tag')
            tagToRemove = Tag.objects.get(id=t)
            u = request.POST.get('user')
            user = User.objects.get(username=u)
            # Remove the tag
            user.favourite_games.remove(t)
            user.save()
    
    # Get the games already selected as their fav games and get a list of ids
    fGames = request.user.favourite_games.all()
    ids = []
    for tag in fGames:
        ids.append(tag.id)

    # Get a list of game tags excluding tags with the ids already in the users fav game
    non_fav_games = Tag.objects.filter(is_game_tag = True).filter(is_pending = False).exclude(id__in=ids).order_by("text")
    context_dict['game_tags'] = non_fav_games
    return render(request, 'settle/account.html', context=context_dict)
