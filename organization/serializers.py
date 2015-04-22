from rest_framework import serializers
from django.contrib.sites.models import Site

from . import models


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
