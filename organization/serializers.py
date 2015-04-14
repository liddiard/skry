from rest_framework import serializers

from . import models


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
