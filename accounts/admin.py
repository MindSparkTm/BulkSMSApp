# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'tag_line')


admin.site.register(UserProfile, UserProfileAdmin)