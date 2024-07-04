
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 200, blank = True)
    content = models.TextField(blank = True)
    author = models.CharField(max_length = 100, default='', blank = True)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    def __str__(self):
        return self.title