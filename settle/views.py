# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from settle.steam_news import get_news
from settle.models import Post, Comment

# Create your views here.

def redirectHome(request):
    response = redirect('/settle')
    return response

def index(request, template="settle/index.html"):
    context_dict = {}
    # author
    # number of comments
    # 1 game tag
    # 2 info tags
    # picture
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'settle/index.html', {'posts': posts})

    # "pic<x>": {
    # "author": "",
    # "comments": <y>,
    # "game": "",
    # "info": [],
    # "img": ""}

def feed(request):
    context_dict = {}

    # need to filter this for feed


def upload(request):
    context_dict = {}
    return render(request, 'settle/upload.html', context=context_dict)


def suggest_tag(request):
    context_dict = {}
    return render(request, 'settle/suggest-tag.html', context=context_dict)


def post(request, post_id):
    context_dict = {}
    result_list = []

    post = Post.objects.filter(id=post_id)

    all_comments = Comment.objects.filter(parent_post=post_id).annotate(num_likes = Count('liking_users')).order_by('-num_likes')

    comm_pagin = Paginator(all_comments, 3) # show 3 comments at once

    page = request.GET.get('page', 1) # get page no. from URL, or 1 if just loading in

    try:
        comments = comm_pagin.page(page) # get the given page of comments
    except PageNotAnInteger:
        comments = comm_pagin.page(1) # default to 1st page if not a number
    except EmptyPage:   
        comments = comm_pagin.page(comm_pagin.num_pages) # default to last page if too big

    # testing - when we actually make it, we'll parameterise the app id
    result_list = get_news(289070, 10)
    # result_list = get_news(440, 5)
    context_dict["result_list"] = result_list
    context_dict["comments"] = comments


    return render(request, 'settle/post.html', context=context_dict)