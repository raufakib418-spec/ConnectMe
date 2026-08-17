from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        max_length=500,
        blank=True
    )

    is_online = models.BooleanField(default=False)

    last_seen = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username