from rest_framework import serializers

from . import models


class CardSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CardSize


class StylesheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Stylesheet


class ScriptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Script


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    stylesheets = StylesheetSerializer(many=True)
    scripts = ScriptSerializer(many=True)

    class Meta:
        model = models.Template
