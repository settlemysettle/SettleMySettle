# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    text = Models.CharField(max_length = 20, unique=True) # 20 character max length, unique, required
    colour = Models.CharField(max_length=6) #6 character hex code - might have ColourField for this instead?
    is_game_tag = Models.BooleanField() # True if game tag, False if info tag
    is_pending = Models.BooleanField() # True if not approved yet, False if approve (and this public)
    steamAppId = Models.IntegerField(default = 0) # Stores Steam App ID for game tags (if applicable)
    
    
    def __str__(self):
        return self.text
