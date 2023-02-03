import json
import os
from django.core.management.base import BaseCommand
from music_library.models import Album, Artist, Track


def import_artists(data):
    for artist_data in data:
        artist = Artist.objects.create(name=artist_data.get("name"),
                                       picture=artist_data.get("picture"))
        artist.save()


def import_albums_and_tracks(data):
    for artist_data in data:
        artist = Artist.objects.get(name=artist_data.get("name"))

        for album_data in artist_data.get("albums", []):
            album = Album.objects.create(title=album_data.get("title"),
                                         cover_art=album_data.get("cover_art"),
                                         artist=artist)
            album.save()

            for track_data in album_data.get("tracks", []):
                featured_artists = track_data.get("featured_artists", [])
                featured_artist_models = []
                if len(featured_artists) > 0:
                    for featured in featured_artists:
                        featured_artist = Artist.objects.get(name=featured)
                        featured_artist_models.append(featured_artist)

                track = Track.objects.create(title=track_data.get("title"),
                                             album=album,
                                             is_hidden=track_data.get(
                                                 "is_hidden", False))
                track.save()
                track.featured_artists.set(featured_artist_models)


class Command(BaseCommand):
    def handle(self, **options):
        curr_dir = os.path.realpath(os.path.dirname(__file__))
        data_filepath = os.path.join(curr_dir, 'data.json')

        with open(data_filepath, 'r') as f:
            data = json.load(f)
            import_artists(data)
            import_albums_and_tracks(data)
            print("Done")
