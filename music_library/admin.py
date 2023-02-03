from django.contrib import admin
from .models import Album, Artist, Track


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    save_as = True
    date_hierarchy = 'updated_on'
    list_filter = ('title', )
    list_display = ('id', 'title')
    readonly_fields = ('id', 'created_on', 'updated_on')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    save_as = True
    date_hierarchy = 'updated_on'
    list_filter = ('name', )
    list_display = ('id', 'name')
    readonly_fields = ('id', 'created_on', 'updated_on')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    save_as = True
    date_hierarchy = 'updated_on'
    list_filter = ('album', )
    list_display = ('id', 'album')
    readonly_fields = ('id', 'created_on', 'updated_on')
