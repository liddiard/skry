from rest_framework import serializers

from ..models import core


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = core.Story
