from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile-images")
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/article-images/")

    def __str__(self):
        return f"{self.title} | {self.category} | {self.published_date.strftime('%Y-%m-%d')}"
