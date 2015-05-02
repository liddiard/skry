from rest_framework import serializers

from authors import serializers as authors_serializers
from attachments import serializers as attachments_serializers
from . import models


class ArtRequestSerializer(serializers.HyperlinkedModelSerializer):
    assignees = authors_serializers.AuthorSerializer(many=True)
    images = attachments_serializers.ImageSerializer(many=True)


class PhotoRequestSerializer(ArtRequestSerializer):
    class Meta:
        model = models.PhotoRequest


class GraphicRequestSerializer(ArtRequestSerializer):
    class Meta:
        model = models.GraphicRequest


class IllustrationRequestSerializer(ArtRequestSerializer):
    class Meta:
        model = models.PhotoRequest
