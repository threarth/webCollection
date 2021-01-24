from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Tablist(models.Model):
#   By default, Django gives each model the following field:
#   id = models.AutoField(primary_key=True)
    named_id = models.CharField(max_length=50, db_index=True)
    artist = models.CharField(max_length=255, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    note = models.CharField(max_length=255, db_index=True)
    count = models.IntegerField()
    chords = models.CharField(max_length=255, db_index=True)
    chords_filename = models.CharField(max_length=255, db_index=True)
    pattern = models.CharField(max_length=255, db_index=True)
    fpath = models.CharField(max_length=255, db_index=True)
    ftype = models.CharField(max_length=25, db_index=True)
    page = models.CharField(max_length=25, db_index=True)
    filecomment = models.CharField(max_length=255, db_index=True)

    def get_absolute_url(self):
        return f'/title/{self.named_id}/'

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
