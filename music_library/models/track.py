import uuid
from django.db import models
from .album import Album
from .artist import Artist


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=300)

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="tracks",
        related_query_name="track",
    )

    featured_artists = models.ManyToManyField(
        Artist,
        related_name="tracks",
        related_query_name="track",
    )

    is_hidden = models.BooleanField(default=False)
