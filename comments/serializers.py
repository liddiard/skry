from rest_framework import serializers

from . import models


class StoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StoryComment


class PhotoRequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoRequest


class GraphicRequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GraphicRequest


class IllustrationRequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IllustrationRequest
