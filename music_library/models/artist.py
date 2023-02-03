import uuid
from django.db import models


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=300)
    picture = models.URLField(blank=True, null=True, default=None)