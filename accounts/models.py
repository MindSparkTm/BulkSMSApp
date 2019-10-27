# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    phone_number = models.CharField(max_length=50)
    tag_line = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'

    def __str__(self):
        return u'{}{}'.format(self.user.first_name, self.user.last_name)
