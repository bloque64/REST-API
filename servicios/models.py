from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



class Article(models.Model):
    is_comment = models.BooleanField(default=False)
    author = models.CharField(max_length=20)
    parent_author = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    token = models.TextField()
    title = models.CharField(max_length=180)
    body = models.TextField()
    image = models.TextField()
    evaluated = models.BooleanField(default=False)
    votes = models.IntegerField()
    down_votes = models.IntegerField()
    permlink = models.TextField()
    parent_permlink = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created',)


class User(models.Model):
    user_name = models.CharField(max_length=180)
    reputation = models.IntegerField()
    profile_image = models.TextField()
    presentation = models.TextField()
    votes = models.IntegerField()
    down_votes = models.IntegerField()
    signup_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('signup_date',)
