# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from settle.fields import ColourField # not sure if this import will work!

# Create your models here.

class Tag(models.Model):
    text = models.CharField(max_length = 20, unique=True) # 20 character max length, unique, required
    colour = ColourField() #hex code, represented by ColourField
    is_game_tag = models.BooleanField() # True if game tag, False if info tag
    is_pending = models.BooleanField() # True if not approved yet, False if approve (and this public)
    steamAppId = models.IntegerField(default = 0) # Stores Steam App ID for game tags (if applicable)
    
    
    def __str__(self):
        return self.text


class User(models.Model):
    username = models.CharField(max_length = 20, unique=True)
    password = models.CharField(max_length = 30)

    favourite_games = models.ManyToManyField(Tag)
    # TODO: implement validation to only allow game tags to be included here.
    # It doesn't seem to be possible in the same way as for the ColourField, since
    # ManyToManyFields are a bit special.
    
