
import os

import django

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

    tags = [civ_6, rimworld, factorio, petra, canada, beginner]

    for tag in tags:
        tag_added = add_tag(tag["text"], tag["colour"], tag["is_game_tag"],
                            tag["is_pending"], tag.get("steamAppId", 0))

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

    for user in users:
        u_added = add_user(user["username"], user["password"], user.get("favourite_games", []))


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
        print(game["text"])
        user.favourite_games.add(Tag.objects.get(text=game["text"]))
    print(user.favourite_games)
    return(user)


"""
def add_post(author, picture, game_tag, info_tags, date_submitted, post_id, description):
    # TODO


def add_comment(author, text, liking_users, parent_post, comment_id):
    # TODO

"""
if __name__ == '__main__':
    print("Populating Settle...")
    populate()
