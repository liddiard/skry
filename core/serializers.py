from rest_framework import serializers

from attachments import serializers as attachments_serializers
from authors import serializers as authors_serializers
from display import serializers as display_serializers
from organization import serializers as organization_serializers
from . import models


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status


class StorySerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    authors = authors_serializers.AuthorSerializer(many=True)
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
    is_published = serializers.SerializerMethodField()
    is_breaking = serializers.SerializerMethodField()

    class Meta:
        model = models.Story
        private_fields = ['assignment_slug', 'status', 'summary', 'angle',
                          'sources', 'late_run', 'created']

    def __init__(self, *args, **kwargs):
        super(StorySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        # remove private fields from response if user is not authenticated
        if request and request.user.is_anonymous():
            for field in self.Meta.private_fields:
                self.fields.pop(field)

    def get_is_published(self, obj):
        return obj.is_published()

    def get_is_breaking(self, obj):
        return obj.is_breaking()


class PageSerializer(serializers.ModelSerializer):
    alternate_template = display_serializers.TemplateSerializer()

    class Meta:
        model = models.Page
