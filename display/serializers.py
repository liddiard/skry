from rest_framework import serializers

from . import models


class CardSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CardSize
        fields = "__all__"


class StylesheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Stylesheet
        fields = "__all__"


class ScriptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Script
        fields = "__all__"


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    stylesheets = StylesheetSerializer(many=True)
    scripts = ScriptSerializer(many=True)

    class Meta:
        model = models.Template
        fields = "__all__"