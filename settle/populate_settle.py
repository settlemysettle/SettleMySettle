from settle.models import Tag, User, Post, Comment
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'settle.settings')

django.setup()


def populate():

    game_tags = [
        {
            "text": "Civ 6",
            "colour": "#FFFF50",
            "is_pending": False,
            "steamAppId": "289070",
        },
        {
            "text": "Factorio",
            "colour": "#C97628",
            "is_pending": False,
            "steamAppId": "427520",
        },
        {
            "text": "Rimworld",
            "colour": "#A2A2A2",
            "is_pending": True,
            "steamAppId": "294100",
        }
    ]

    info_tags = [
        {
            "text": "Petra",
            "colour": "#F3AF50",
            "is_pending": False,
        },
        {
            "text": "Canada",
            "colour": "#FF1000",
            "is_pending": False,
        },
        {
            "text": "Beginner",
            "colour": "#11EE11",
            "is_pending": False,
        },
    ]


def add_tag(text, colour, is_game_tag, is_pending, steamAppId):
    # adds tag
    j = 2


def add_user(username, password, favourite_games):


def add_post(author, picture, game_tag, info_tags, date_submitted, post_id, description):


def add_comment(author, text, liking_users, parent_post, comment_id):
