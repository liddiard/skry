from rest_framework import serializers

from . import models


class SportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sport
        fields = "__all__"


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.School
        fields = "__all__"


class GameSerializer(serializers.HyperlinkedModelSerializer):
    sport = SportSerializer()
    home = SchoolSerializer()
    opposing = SchoolSerializer()

    class Meta:
        model = models.Game
        fields = "__all__"
