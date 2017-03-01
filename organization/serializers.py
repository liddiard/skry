from rest_framework import serializers
from django.contrib.sites.models import Site

from . import models


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Section
        fields = "__all__"


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"
