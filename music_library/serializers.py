from rest_framework import serializers
from .models import Album, Artist, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta():
        model = Track
        fields = ['album']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta():
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta():
        model = Album
        fields = '__all__'
