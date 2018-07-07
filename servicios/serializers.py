from django.forms import widgets
from rest_framework import serializers
from servicios.models import Article
from servicios.models import User




class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'is_comment', 'author', 'parent_author', 'category', 'token', 'title', 'body', 'image', 'evaluated',  'votes', 'down_votes', 'permlink', 'parent_permlink', 'created')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'reputation' , 'profile_image', 'presentation', 'votes', 'down_votes', 'signup_date')
