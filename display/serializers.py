from rest_framework import serializers

from . import models


class CardSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardSize


class StylesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stylesheet


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Script


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Template
