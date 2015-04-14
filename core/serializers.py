from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Story


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
