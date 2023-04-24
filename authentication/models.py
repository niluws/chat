from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html

from utils.models import AbstracId


class User(AbstractUser, AbstracId):
    email = models.EmailField(max_length=256, null=True, blank=True, unique=True)
    birth_date = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    active_code = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='user/photo', default='user/photo/default.png')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

    def img(self):
        return format_html("<img style='width:30px;border-radius:50%;' src='{}'>".format(self.photo.url))
