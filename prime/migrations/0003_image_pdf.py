# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '__first__'),
        ('prime', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=prime.models.get_image_upload_path)),
                ('issue', models.ForeignKey(default=None, to_field='id', blank=True, to='prime.Issue', null=True)),
                ('author', models.ForeignKey(to_field='id', blank=True, to='news.Author', null=True)),
                ('caption', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pdf', models.FileField(upload_to=prime.models.get_pdf_upload_path)),
                ('image', models.ImageField(upload_to=prime.models.get_pdf_image_upload_path)),
                ('issue', models.OneToOneField(to='prime.Issue', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
