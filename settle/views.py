# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from settle.steam_news import get_news

# Create your views here.

def redirectHome(request):
    response = redirect('/settle')
    return response

def index(request):
    context_dict = {}
    context_dict["boldmessage"] = "Hi there from views! :D"
    return render(request, 'settle/index.html', context=context_dict)


def feed(request):
    context_dict = {}
    return render(request, 'settle/feed.html', context=context_dict)


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
    result_list = get_news(289070, 3)
    context_dict["result_list"] = result_list


    return render(request, 'settle/post.html', context=context_dict)