from rest_framework import serializers

from . import models


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sport


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School


class GameSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    home = SchoolSerializer()
    opposing = SchoolSerializer()

    class Meta:
        model = models.School
