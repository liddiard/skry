from rest_framework import serializers

from core import serializers as core_serializers
from . import models


class MediaSerializer(serializers.ModelSerializer):
    credit = core_serializers.AuthorSerializer(many=True)


class ImageSerializer(MediaSerializer):
    class Meta:
        model = models.Image


class VideoSerializer(MediaSerializer):
    class Meta:
        model = models.Video


class AudioSerializer(MediaSerializer):
    class Meta:
        model = models.Audio


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Poll


class PollChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PollChoice
