# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('description', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('featured_image', models.ImageField(upload_to=b'research/project/featured_image')),
                ('github', models.URLField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('authors', models.ManyToManyField(to='news.Author')),
            ],
            options={
                'ordering': (b'-published',),
            },
            bases=(models.Model,),
        ),
    ]
