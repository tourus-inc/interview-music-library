import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.URLField(blank=True, null=True, default=None)
    nickname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
