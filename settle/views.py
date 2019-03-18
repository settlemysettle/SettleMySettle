# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from settle.steam_news import get_news
from settle.models import Post, Comment, Tag, User
from settle.forms import SignupForm, CommentForm, UploadForm
from django import forms
from django.utils import timezone
from settle.validators import CPasswordValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password

# Create your views here.


def redirectHome(request):
    response = redirect('/settle')
    return response


def index(request, template="settle/index.html"):
    context_dict = {}
    post_list = Post.objects.all().order_by("-date_submitted")
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'settle/index.html', {'posts': posts})


def feed(request):
    context_dict = {}

    # need to filter this for feed
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'settle/feed.html', {'posts': posts})


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


def suggest_tag(request):
    context_dict = {}
    return render(request, 'settle/suggest-tag.html', context=context_dict)


def post(request, post_id):
    context_dict = {}
    result_list = []

    post = Post.objects.filter(id=post_id)[0]

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

    # testing - when we actually make it, we'll parameterise the app id

    app_id = post.game_tag.steamAppId

    if app_id != 0:
        result_list = get_news(app_id, 10)
    # result_list = get_news(440, 5)
    context_dict["result_list"] = result_list
    context_dict["post"] = post
    context_dict["comments"] = comments
    context_dict["comment_count"] = comment_count

    if request.method == 'POST':
        # Use the signup_form
        comment_form = CommentForm(data=request.POST)
        context_dict['form'] = comment_form

        # Check the data given is valid
        if comment_form.is_valid():
            # Get the user from the form
            newComment = comment_form.save(commit=False)
            # Get the cleaned data
            text = comment_form.cleaned_data['text']
            newComment.save()
        else:
            # Print the errors from the form
            print(comment_form.errors)
    else:
        # Give it back an empty form
        comment_form = CommentForm()
        context_dict['form'] = comment_form

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

        else:
            # Print the errors from the form
            print(signup_form.errors)
    else:
        # Give it back an empty form
        signup_form = SignupForm()

    return render(request, 'settle/register.html', {'form': signup_form, 'registered': registered})

def user_login(request):
    # If request is post, pull out relevent data
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
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'settle/index.html', {})

