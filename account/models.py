from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    image = models.ImageField(default="profile.jpg", null=True, blank=True, upload_to="profile-pic")
    def __str__(self):
        return self.name