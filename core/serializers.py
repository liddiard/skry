from rest_framework import serializers

from . import models


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Story
        depth = 1
