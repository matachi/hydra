# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('date', models.CharField(max_length=50)),
                ('source_code', models.URLField(blank=True)),
                ('license', models.CharField(blank=True, max_length=50)),
                ('title_image', models.ImageField(upload_to=projects.models.title_image_filename, storage=projects.models.OverwriteStorage())),
                ('libraries', models.ManyToManyField(related_name='projects', to='projects.Library', blank=True)),
                ('platforms', models.ManyToManyField(related_name='projects', to='projects.Platform')),
                ('programming_languages', models.ManyToManyField(related_name='projects', to='projects.ProgrammingLanguage', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('large', models.ImageField(blank=True, upload_to=projects.models.large_filename, storage=projects.models.OverwriteStorage())),
                ('thumbnail', models.ImageField(blank=True, upload_to=projects.models.thumbnail_filename, storage=projects.models.OverwriteStorage())),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='screenshots',
            field=models.ManyToManyField(related_name='projects', to='projects.Screenshot', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(related_name='projects', to='projects.Tool', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='project',
            field=models.ForeignKey(related_name='links', to='projects.Project'),
            preserve_default=True,
        ),
    ]
