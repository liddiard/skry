# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'news/image/%Y/%m/%d/original/')),
                ('image_full', models.ImageField(upload_to=b'news/image/%Y/%m/%d/full/1x/')),
                ('image_full_2x', models.ImageField(upload_to=b'news/image/%Y/%m/%d/full/2x/')),
                ('image_float', models.ImageField(upload_to=b'news/image/%Y/%m/%d/float/1x/')),
                ('image_float_2x', models.ImageField(upload_to=b'news/image/%Y/%m/%d/float/2x/')),
                ('image_card', models.ImageField(null=True, upload_to=b'news/image/%Y/%m/%d/card/1x/', blank=True)),
                ('image_card_2x', models.ImageField(null=True, upload_to=b'news/image/%Y/%m/%d/card/2x/', blank=True)),
                ('credit', models.ManyToManyField(to='news.Author', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(to='news.Poll', to_field='id')),
                ('choice', models.CharField(max_length=128)),
                ('votes', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
