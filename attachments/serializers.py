from rest_framework import serializers

from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video


class AudioSerializer(serializers.ModelSerializer):
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
