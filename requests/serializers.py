from rest_framework import serializers

from . import models


class PhotoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoRequest


class GraphicRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GraphicRequest


class IllustrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoRequest
