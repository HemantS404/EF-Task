from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='ProfilePictures/')
    bio = models.CharField(default="", max_length = 100, blank = True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.username