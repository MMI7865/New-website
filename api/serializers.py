from rest_framework import serializers
from .models import User, Article, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [  
                    'id', 'username', 
                    'first_name', 'last_name', 
                    'email', 'profile_pic', 'date_of_birth'
                 ]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
                    'id', 'title', 
                    'tag', 'content', 'category', 
                    'author', 'published_date', 'image'
                 ]