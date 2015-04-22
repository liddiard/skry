from rest_framework import serializers
from django.contrib.sites.models import Site

from . import models


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Section


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
