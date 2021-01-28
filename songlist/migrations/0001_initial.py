# Generated by Django 3.1.5 on 2021-01-28 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('year', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('artist_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Tablist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('db', models.CharField(db_index=True, max_length=255)),
                ('sid', models.IntegerField(db_index=True)),
                ('artist', models.CharField(db_index=True, max_length=255)),
                ('songbook', models.CharField(db_index=True, max_length=255)),
                ('type', models.CharField(db_index=True, max_length=255)),
                ('count', models.IntegerField(db_index=True)),
                ('chords', models.CharField(db_index=True, max_length=255)),
                ('to_study', models.CharField(db_index=True, max_length=255)),
                ('rank', models.IntegerField(db_index=True)),
                ('db_name', models.CharField(db_index=True, max_length=255)),
                ('db_source', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('index', models.IntegerField()),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='songlist.album')),
            ],
            options={
                'ordering': ('index',),
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songlist.artist'),
        ),
    ]
