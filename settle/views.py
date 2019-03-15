# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from settle.models import Post
from settle.steam_news import get_news

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
    numbers_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 3)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'settle/index.html', {'numbers': numbers})

    # "pic<x>": {
    # "author": "",
    # "comments": <y>,
    # "game": "",
    # "info": [],
    # "img": ""}

def feed(request):
    context_dict = {}

    # need to filter this for feed
    numbers_list = Post.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 3)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'settle/feed.html', {'numbers': numbers})


def upload(request):
    context_dict = {}
    return render(request, 'settle/upload.html', context=context_dict)


def suggest_tag(request):
    context_dict = {}
    return render(request, 'settle/suggest-tag.html', context=context_dict)


def post(request):
    context_dict = {}
    result_list = []

    # testing - when we actually make it, we'll parameterise the app id
    result_list = get_news(289070, 10)
    # result_list = get_news(440, 5)
    context_dict["result_list"] = result_list


    return render(request, 'settle/post.html', context=context_dict)