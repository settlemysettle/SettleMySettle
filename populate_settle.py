
import os

import django

from PIL import Image
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'settle_my_settle.settings')


django.setup()

from settle.models import Tag, User, Post, Comment


def populate():

    # TAGS

    civ_6 = {
        "text": "Civ 6",
        "colour": "#FFFF50",
        "is_pending": False,
        "is_game_tag": True,
        "steamAppId": "289070",
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

    petra = {
        "text": "Petra",
        "colour": "#F3AF50",
        "is_pending": False,
        "is_game_tag": False,
    }

    canada = {
        "text": "Canada",
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

    tags = [civ_6, rimworld, factorio, alpha, petra, canada, beginner]


    # USERS
    secure_user = {
        "username": "VerySecureUser",
        "password": "Luk3",
        "favourite_games": [civ_6]
    }

    mid_seier = {
        "username": "MidSeier",
        "password": "fire axes",
        "favourite_games": [rimworld, factorio]
    }

    contrarian = {
        "username": "EverythingIsAwful",
        "password": "it'll get hacked anyway",
    }

    users = [secure_user, mid_seier, contrarian]

    
    


    #centauri_im = Image.open("centauri.png")

    # POSTS
    centauri = {
        "author": secure_user,
        "picture": "centauri.png",
        "game_tag": alpha,
        "info_tags": [beginner],
        "description": "If you haven't played this game, check it out! For a 20 year old game," + 
                       "the UI is surprisingly snappy and it's quite a well grounded depiction of future-era technology.",
        
    }

    #niani_im = Image.open("niani.png")

    niani = {
        "author": mid_seier,
        "picture": "niani.png",
        "game_tag": civ_6,
        "info_tags": [petra],
        "description": "A really nice start for my first Gathering Storm game! The gold is rolling in now.",      
    }
    
    posts = [centauri, niani]

    for tag in tags:
        tag_added = add_tag(tag["text"], tag["colour"], tag["is_game_tag"],
                            tag["is_pending"], tag.get("steamAppId", 0))

    for user in users:
        user_added = add_user(user["username"], user["password"], user.get("favourite_games", []))
    
    
    print("----")
    print("adding posts")
    print("----")
    for post in posts:
        post_added = add_post(post["author"], post["picture"], post["game_tag"], post["info_tags"], post["description"])



def add_tag(text, colour, is_game_tag, is_pending, steamAppId):
    # adds tag
    tag = Tag.objects.get_or_create(
        text=text, colour=colour, is_game_tag=is_game_tag, is_pending=is_pending, steamAppId=steamAppId)[0]
    tag.save()
    return(tag)


def add_user(username, password, favourite_games):
    user = User.objects.get_or_create(username=username, password=password)[0]
    user.save()
    for game in favourite_games:
        user.favourite_games.add(Tag.objects.get(text=game["text"]))
    print(user.favourite_games.all())
    return(user)


def add_post(author, picture, game_tag, info_tags, description):
    print("post being added?")
    post = Post.objects.get_or_create(description=description, picture=picture)[0]
    post.save()
  
    print("adding game tag...")
    post.game_Tag.add(Tag.objects.get(text=game_tag["text"]))

    for info_tag in info_tags:
        post.info_tags.add(Tag.objects.get(text=info_tag["text"]))

    print("checking author...")

    post.author = User.objects.get(username=author["username"])

    return(post)

"""
def add_comment(author, text, liking_users, parent_post, comment_id):
    # TODO

"""
if __name__ == '__main__':
    print("Populating Settle...")
    populate()
