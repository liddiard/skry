from rest_framework import serializers

from authors import serializers as authors_serializers
from . import models


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    credit = authors_serializers.AuthorSerializer(many=True)


class ImageSerializer(MediaSerializer):
    class Meta:
        model = models.Image


class VideoSerializer(MediaSerializer):
    class Meta:
        model = models.Video


class AudioSerializer(MediaSerializer):
    class Meta:
        model = models.Audio


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Review


class PollChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PollChoice


class PollSerializer(serializers.HyperlinkedModelSerializer):
    pollchoice_set = PollChoiceSerializer(many=True)
        # TODO: figure out how to change this field name to something nicer,
        # like "choices"

    class Meta:
        model = models.Poll
        fields = ('question', 'is_open', 'pollchoice_set')
