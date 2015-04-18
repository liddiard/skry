from rest_framework import serializers

from access import serializers as access_serializers
from attachments import serializers as attachments_serializers
from display import serializers as display_serializers
from organization import serializers as organization_serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    user = access_serializers.UserSerializer()

    class Meta:
        model = models.Author


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status


class StorySerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    authors = AuthorSerializer(many=True)
    alternate_template = display_serializers.TemplateSerializer()
    sections = organization_serializers.SectionSerializer(many=True)
    tags = organization_serializers.TagSerializer(many=True)
    card = attachments_serializers.ImageSerializer()
    card_size = display_serializers.CardSizeSerializer()
    featured_image = attachments_serializers.ImageSerializer()
    featured_video = attachments_serializers.VideoSerializer()
    featured_audio = attachments_serializers.AudioSerializer()
    review = attachments_serializers.ReviewSerializer()
    poll = attachments_serializers.PollSerializer()

    class Meta:
        model = models.Story


class PageSerializer(serializers.ModelSerializer):
    alternate_template = display_serializers.TemplateSerializer()

    class Meta:
        model = models.Page
