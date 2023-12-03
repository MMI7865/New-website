from django.contrib import admin
from .models import User, Article, Category

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Category)