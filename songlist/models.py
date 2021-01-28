from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Tablist(models.Model):
#   By default, Django gives each model the following field:
#   id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, db_index=True)
    db = models.CharField(max_length=255, db_index=True)
    sid = models.IntegerField(db_index=True)
    artist = models.CharField(max_length=255, db_index=True)
    songbook = models.CharField(max_length=255, db_index=True)
    type = models.CharField(max_length=255, db_index=True)
    count = models.IntegerField(db_index=True)
    chords = models.CharField(max_length=255, db_index=True)
    to_study = models.CharField(max_length=255, db_index=True)
    rank = models.IntegerField(db_index=True)
    db_name = models.CharField(max_length=255, db_index=True)

    def get_absolute_url(self):
        return f'http://www.grilliconsulting.com/a/music/viewer.html?id={self.sid}&db={self.db_name}'

class Artist(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Album(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='albums'
    )
    year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )

class Track(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    index = models.IntegerField()
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='tracks'
    )
    duration = models.CharField(
        max_length=255,
        db_index=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('index',)


class Song(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.song_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
