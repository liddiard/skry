from rest_framework import serializers

from . import models


class CardSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardSize


class IncludeCSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IncludeCSS


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Template
