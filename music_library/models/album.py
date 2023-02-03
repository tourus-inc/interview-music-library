import uuid
from django.db import models
from .artist import Artist


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=300)
    cover_art = models.URLField(blank=True, null=True, default=None)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="albums",
        related_query_name="album",
    )
