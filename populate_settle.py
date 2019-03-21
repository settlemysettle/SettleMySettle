
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'settle_my_settle.settings')

django.setup()

from settle.models import Tag, User, Post, Comment


import django
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from PIL import Image
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'settle_my_settle.settings')


django.setup()


def populate():

    admin, created = Group.objects.get_or_create(name='admin') # make an admin group if it doesn't exist already

    # TAGS

    civ_6 = {
        "text": "Civ 6",
        "colour": "#FFFF50",
        "is_pending": False,
        "is_game_tag": True,
        "steamAppId": "289070",
    }
    civ_5 = {
        "text": "Civ 5",
        "colour": "#D4AFB9",
        "is_pending": False,
        "is_game_tag": True,
        "steamAppId": "8930",
    }
    civ_3 = {
        "text": "Civ 3",
        "colour": "#D8D8D8",
        "is_pending": False,
        "is_game_tag": True,
        "steamAppId": "3910",
    }
    factorio = {
        "text": "Factorio",
        "colour": "#C97628",
        "is_pending": False,
        "is_game_tag": True,
        "steamAppId": "427520",
    }
    rimworld = {
        "text": "Rimworld",
        "colour": "#A2A2A2",
        "is_pending": True,
        "is_game_tag": True,
        "steamAppId": "294100",
    }
    alpha = {
        "text": "Alpha Centauri",
        "colour": "#9B5039",
        "is_pending": True,
        "is_game_tag": True,
    }

    fortnite = {
        "text": "Fortnite",
        "colour": '#4c51f7',
        "is_pending": True,
        "is_game_tag": True,
    }

    petra = {
        "text": "Petra",
        "colour": "#F3AF50",
        "is_pending": False,
        "is_game_tag": False,
    }

    england = {
        "text": "England",
        "colour": "#FF1000",
        "is_pending": False,
        "is_game_tag": False,
    }

    beginner = {
        "text": "Beginner",
        "colour": "#11EE11",
        "is_pending": False,
        "is_game_tag": False,
    }

    tags = [civ_6, civ_5, civ_3, rimworld,
            factorio, alpha, fortnite, petra, england, beginner]

    # USERS
    secure_user = {
        "username": "VerySecureUser",
        "password": "Luk3",
        "email": "verysecure@hotmail.co.uk",
        "favourite_games": [civ_6]
    }

    apex = {
        "username": "ApexBoy",
        "password": "F0rtnit3",
        "email": "battleroyale@ntlworld.com",
    }

    mid_seier = {
        "username": "MidSeier",
        "password": "fire axes",
        "email": "civ5forever@hotmail.co.uk",
        "favourite_games": [rimworld, factorio],
        "is_admin": True
    }

    contrarian = {
        "username": "EverythingIsAwful",
        "password": "it'll get hacked anyway",
        "email": "tetris99@hotmail.co.uk",
    }

    users = [secure_user, mid_seier, contrarian, apex]

    # POSTS
    centauri = {
        "author": secure_user,
        "picture": "centauri.png",
        "game_tag": alpha,
        "info_tags": [beginner],
        "description": "If you haven't played this game, check it out! For a 20 year old game," +
                       "the UI is surprisingly snappy and it's quite a well grounded depiction of future-era technology.",

    }

    niani = {
        "author": mid_seier,
        "picture": "niani.png",
        "game_tag": civ_6,
        "info_tags": [petra],
        "description": "A really nice start for my first Gathering Storm game! " +
        "The gold is rolling in now.",
    }

    bigCity = {
        "author": contrarian,
        "picture": "bigCity.png",
        "game_tag": civ_6,
        "info_tags": [petra, beginner],
        "description": "Made a great city to support the best lecturer this year"
    }

    civ3celts = {
        "author": contrarian,
        "picture": "civ3Celts.png",
        "game_tag": civ_3,
        "info_tags": [england],
        "description": "Start of a game in civ 3"
    }

    civ5_2 = {
        "author": mid_seier,
        "picture": "civ5-2.png",
        "game_tag": civ_5,
        "info_tags": [england, beginner],
        "description": "Great civ 5 game so far!!"
    }

    civ5London = {
        "author": secure_user,
        "picture": "civ5London.png",
        "game_tag": civ_5,
        "info_tags": [england],
        "description": "11:05pm, March 29th 2019 (colourised)"
    }

    factorio1 = {
        "author": mid_seier,
        "picture": "factorio1.png",
        "game_tag": factorio,
        "info_tags": [beginner],
        "description": "Who even plays civ these days?"
    }

    factorio2 = {
        "author": contrarian,
        "picture": "factorio2.png",
        "game_tag": factorio,
        "info_tags": [petra],
        "description": "Not sure if I like this game..."
    }

    lukeEngland = {
        "author": secure_user,
        "picture": "lukeEngland.png",
        "game_tag": civ_6,
        "info_tags": [england, petra],
        "description": "Started really good, think I might win!"
    }

    melbourne = {
        "author": mid_seier,
        "picture": "melbourne.png",
        "game_tag": civ_6,
        "info_tags": [petra],
        "description": "Playing as Australia!"
    }

    bad_post = {
        "author": mid_seier,
        "picture": "apex.jpg",
        "game_tag": civ_5,
        "info_tags": [],
        "description": "Please give me apex coins, my hero is very sick"
    }

    newCiv6 = {
        "author": contrarian,
        "picture": "newCiv6.png",
        "game_tag": civ_6,
        "info_tags": [beginner],
        "description": "Not sure what I'm doing here"
    }

    rimworld1 = {
        "author": mid_seier,
        "picture": "rimworld1.png",
        "game_tag": rimworld,
        "info_tags": [beginner],
        "description": "Just started playing Rimworld! It's great!"
    }

    rimworld2 = {
        "author": contrarian,
        "picture": "rimworld2.png",
        "game_tag": rimworld,
        "info_tags": [petra],
        "description": "What a great game so far"
    }

    wad = {
        "author": secure_user,
        "picture": "wad.png",
        "game_tag": civ_6,
        "info_tags": [petra, beginner, england],
        "description": "What an absolute unit of a mountain"
    }

    posts = [centauri, niani, bigCity, civ3celts, civ5_2, factorio1,
             factorio2, lukeEngland, melbourne, newCiv6, bad_post, rimworld1, rimworld2, wad, civ5London]

    lond_comm_1 = {
        "author": mid_seier,
        "text": "Nice work getting past the Great Wall! It's pretty tough at that stage in the game.",
        "liking_users": [secure_user, contrarian],
        "parent_post": civ5London,
    }

    lond_comm_2 = {
        "author": contrarian,
        "text": "Perhaps it's better not to ask how the elephants crossed the Channel...",
        "liking_users": [secure_user],
        "parent_post": civ5London,
    }

    lond_comm_3 = {
        "author": mid_seier,
        "text": "pls dont hurt the deer",
        "liking_users": [],
        "parent_post": civ5London,
    }

    lond_comm_4 = {
        "author": secure_user,
        "text": "Update: Things are going pretty okay at the moment!",
        "liking_users": [secure_user],
        "parent_post": civ5London,
    }

    cent_comment = {
        "author": mid_seier,
        "text": "The manual of this game's pretty amazing as well - 250 pages of " +
                "instructions, strategies and even biological information about " +
                "the planet you're playing on. Check it out if you can!",
        "liking_users": [secure_user, contrarian],
        "parent_post": centauri,
    }

    cent_reply = {
        "author": secure_user,
        "text": "The manual's pretty great! The digital version comes with a PDF of the manual. Imagine what it would be" +
                "like to have a physical copy of that thing.",
        "liking_users": [mid_seier],
        "parent_post": centauri,
    }

    cent_retort = {
        "author": mid_seier,
        "text": "I owned a physical copy back in 1999! It was a christmas present, and a rather great " +
                "one at that. But we moved out and unfortunately I lost it...",
        "parent_post": centauri,
    }

    cent_comeback = {
        "author": secure_user,
        "text": "That's got to be awful! At least thanks to digital copies you never have to worry about losing it now.",
        "liking_users": [mid_seier],
        "parent_post": centauri,
    }
    
    bad_comment = {
        "author": apex,
        "text": "just play fortnite instead lol",
        "parent_post": centauri,
    }

    niani_comment = {
        "author": contrarian,
        "text": "Why are you playing on strategic view? It's so ugly in this game, " +
                "Civ 5 was way better in that regard.",
        "parent_post": niani,
    }

    comments = [cent_comment, cent_reply,
                cent_retort, cent_comeback, bad_comment, niani_comment, lond_comm_1, lond_comm_2, lond_comm_3,
                lond_comm_4]

    for tag in tags:
        tag_added = add_tag(tag["text"], tag["colour"], tag["is_game_tag"],
                            tag["is_pending"], tag.get("steamAppId", 0))

    for user in users:
        user_added = add_user(
            user["username"], user["password"], user["email"], user.get("favourite_games", []), user.get("is_admin", False))

    for post in posts:
        post_added = add_post(post["author"], post["picture"],
                              post["game_tag"], post["info_tags"], post["description"])

    for comment in comments:
        comment_added = add_comment(comment["author"], comment["text"], comment.get(
            "liking_users", []), comment["parent_post"])


def add_tag(text, colour, is_game_tag, is_pending, steamAppId):
    # adds tag
    tag = Tag.objects.get_or_create(
        text=text, colour=colour, is_game_tag=is_game_tag, is_pending=is_pending, steamAppId=steamAppId)[0]
    tag.save()
    return(tag)


def add_user(username, password, email, favourite_games, is_admin):
    user = User.objects.get_or_create(username=username, password=make_password(
        password, hasher="pbkdf2_sha256"), email=email)[0]
    user.save()
    for game in favourite_games:
        user.favourite_games.add(Tag.objects.get(text=game["text"]))

    if is_admin:
        admin = Group.objects.get(name='admin') 
        admin.user_set.add(user)
    print(user.favourite_games.all())
    return(user)


def add_post(author, picture, game_tag, info_tags, description):
    auth = User.objects.get(username=author["username"])
    game_t = Tag.objects.get(text=game_tag["text"])

    post = Post.objects.get_or_create(
        author=auth, game_tag=game_t, description=description, picture=picture)[0]
    post.save()

    for info_tag in info_tags:
        post.info_tags.add(Tag.objects.get(text=info_tag["text"]))

    post.author = User.objects.get(username=author["username"])

    return(post)


def add_comment(author, text, liking_users, parent_post):
    auth = User.objects.get(username=author["username"])
    par_post = Post.objects.get(picture=parent_post["picture"])

    comment = Comment.objects.get_or_create(
        author=auth, text=text, parent_post=par_post)[0]
    comment.save()

    for l_user in liking_users:
        comment.liking_users.add(User.objects.get(username=l_user["username"]))

    return(comment)


if __name__ == '__main__':
    print("Populating Settle...")
    populate()
    print("Done!")
