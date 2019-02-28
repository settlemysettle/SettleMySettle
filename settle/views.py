# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Hi from the view for index! :D"}
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