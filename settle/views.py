# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from settle.steam_news import get_news
from settle.models import Post, Comment

# Create your views here.

def redirectHome(request):
    response = redirect('/settle')
    return response

def index(request):
    context_dict = {}
    # author
    # number of comments
    # 1 game tag
    # 2 info tags
    # picture
    context_dict["pictures"] = [
        
        [
            {
                "author": "Sarah",
                "comments": 4012,
                "game": "Lab",
                "info": ["big", "dog"],
                "img": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.15752-9/53657236_2029507903811903_6665021578117382144_n.jpg?_nc_cat=101&_nc_ht=scontent-lhr3-1.xx&oh=3d7c2d925abeaad8a3b7ff5b8c171620&oe=5D159C73"
            },
            {
                "author": "Luke",
                "comments": 5,
                "game": "Dog",
                "info": ["good", "boi"],
                "img": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.15752-9/53226239_782870245439195_5639702418003329024_n.jpg?_nc_cat=101&_nc_ht=scontent-lhr3-1.xx&oh=5b28b63d40622d7aed3de5eedcf8f3dd&oe=5D216AD6"
            },
            {
                "author": "Lewis",
                "comments": 14,
                "game": "Factorio",
                "info": [],
                "img": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.15752-9/53309035_422858091839343_7339374590830837760_n.jpg?_nc_cat=107&_nc_ht=scontent-lhr3-1.xx&oh=ab3c48cb44d3ebe1b926b2fcee9facac&oe=5D14D55D"
            }
        ],
        [
            {
                "author": "JohnDavis1302",
                "comments": 10,
                "game": "Civ6",
                "info": ["Canada", "Desert"],
                "img": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.15752-9/53713833_410891662815291_5324056544046743552_n.jpg?_nc_cat=111&_nc_ht=scontent-lhr3-1.xx&oh=00ec11a0bbd864f28aa45168f3b3d679&oe=5D200385"
            },
            {
                "author": "Leewman99",
                "comments": 214,
                "game": "Alpha",
                "info": ["Alien", "Small"],
                "img": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.15752-9/53233389_393228021472472_6765313995101437952_n.jpg?_nc_cat=104&_nc_ht=scontent-lhr3-1.xx&oh=01704cbd90a0bbae3ccb0c8985e354e8&oe=5D1CAA5F"
            },
            {
                "author": "StrategyFan400",
                "comments": 12,
                "game": "Civ5",
                "info": ["Poland", "Large"],
                "img": "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.15752-9/53839907_434621970611227_6944686586890027008_n.jpg?_nc_cat=109&_nc_ht=scontent-lhr3-1.xx&oh=915b3fdafc47cba68671194db0b05367&oe=5D16F4D3"
            }
        ]
    ]

    return render(request, 'settle/index.html', context=context_dict)

    # "pic<x>": {
    # "author": "",
    # "comments": <y>,
    # "game": "",
    # "info": [],
    # "img": ""}

def feed(request):
    context_dict = {}
    return render(request, 'settle/feed.html', context=context_dict)


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

    all_comments = Comment.objects.filter(parent_post=post_id)

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