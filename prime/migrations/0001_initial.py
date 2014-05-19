# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import prime.models 


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('release_date', models.DateField()),
                ('header_image', models.ImageField(null=True, upload_to=prime.models.get_issue_upload_path, blank=True)),
            ],
            options={
                'ordering': [b'release_date'],
            },
            bases=(models.Model,),
        ),
    ]
