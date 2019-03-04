
from settle.models import Tag, User, Post, Comment
import os

import django
from django.conf import settings

if not settings.configured:
    settings.configure(settle_defaults, DEBUG=True)


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'settle_my_settle.settings')


django.setup()


def populate():

    # TAGS

    tags = [
        {
            "text": "Civ 6",
            "colour": "#FFFF50",
            "is_pending": False,
            "is_game_tag": True,
            "steamAppId": "289070",
        },
        {
            "text": "Factorio",
            "colour": "#C97628",
            "is_pending": False,
            "is_game_tag": True,
            "steamAppId": "427520",
        },
        {
            "text": "Rimworld",
            "colour": "#A2A2A2",
            "is_pending": True,
            "is_game_tag": True,
            "steamAppId": "294100",
        },
        {
            "text": "Petra",
            "colour": "#F3AF50",
            "is_pending": False,
            "is_game_tag": False,
        },
        {
            "text": "Canada",
            "colour": "#FF1000",
            "is_pending": False,
            "is_game_tag": False,
        },
        {
            "text": "Beginner",
            "colour": "#11EE11",
            "is_pending": False,
            "is_game_tag": False,
        },
    ]

    for tag in tags:
        t = add_tag(t["text"], t["colour"], t["is_game_tag"],
                    t["is_pending"], t.get("steamAppId", 0))


def add_tag(text, colour, is_game_tag, is_pending, steamAppId):
    # adds tag
    tag = Tag.objects.get_or_create(
        text=text, colour=colour, is_game_tag=is_game_tag, is_pending=is_pending, steamAppId=steamAppId)[0]
    tag.save()
    return(tag)


"""
def add_user(username, password, favourite_games):
    # TODO


def add_post(author, picture, game_tag, info_tags, date_submitted, post_id, description):
    # TODO


def add_comment(author, text, liking_users, parent_post, comment_id):
    # TODO

"""
if __name__ == '__main__':
    print("Populating Settle...")
    populate()
