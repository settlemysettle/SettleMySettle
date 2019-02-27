# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from settle.models import Tag, User, Post, Comment

admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
