import logging

logger = logging.getLogger(__name__)

from rest_framework import viewsets

from .models import Album, Artist, Track
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    model = Album
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.all()


class ArtistViewSet(viewsets.ModelViewSet):
    model = Artist
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class TrackViewSet(viewsets.ModelViewSet):
    model = Track
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
