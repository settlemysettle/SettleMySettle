# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from settle.fields import ColourField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    # 20 character max length, unique, required
    text = models.CharField(max_length=20, unique=True)
    colour = ColourField()  # hex code, represented by ColourField
    is_game_tag = models.BooleanField()  # True if game tag, False if info tag
    # True if not approved yet, False if approve (and this public)
    is_pending = models.BooleanField()
    # Stores Steam App ID for game tags (if applicable)
    steamAppId = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.text


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)

    REQUIRED_FIELDS = []
    favourite_games = models.ManyToManyField(Tag)
    # TODO: implement validation to only allow game tags to be included here.
    # It doesn't seem to be possible in the same way as for the ColourField, since
    # ManyToManyFields are a bit special.

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # is CASCADE okay here? When we delete a user, should their posts disappear too?
    # I'll say so for now, but subject to change.
    # Perhaps make a default "anonymous" user we revert to if a user is deleted?
    picture = models.ImageField()
    game_tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, related_name='post_game')
    # same story as above, but a bit less sure this time - default makes little sense
    # I think cascade is probably the best option from a bad bunch
    info_tags = models.ManyToManyField(
        Tag, related_name='post_infos', blank=True)
    # how to validate this server-side?
    # use DateTime for multiple posts on same day
    date_submitted = models.DateTimeField(default=timezone.now)
    #post_id = models.AutoField(primary_key=True)
    # or we could just use post_id to sort? could cause problems w/ deleted posts through
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return str(str(self.date_submitted) + ": by " + str(self.author))


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='com_author')

    text = models.CharField(max_length=300)

    liking_users = models.ManyToManyField(
        User, related_name='com_likers', blank=True)

    parent_post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    # post doesn't care if a comment is deleted

    def __str__(self):
        return (self.text + " by " + str(self.author))
