from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.contenttypes.models import ContentType

from authors import serializers as authors_serializers
from . import models


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    credit = authors_serializers.AuthorSerializer(many=True)


class ImageSerializer(MediaSerializer):
    resized = serializers.SerializerMethodField()
    request = serializers.SerializerMethodField()

    class Meta:
        model = models.Image
        exclude = ('content_type', 'object_id')

    def get_resized(self, obj):
        """Provides the ability to specify optional resolution and crop
        parameters to return a URL to a resized version."""

        request = self.context['request']
        resolution = request.GET.get('resolution')
        crop = request.GET.get('crop')
        if resolution and crop:
            return obj.get_image_at_resolution(resolution, crop=crop)
        elif resolution:
            return obj.get_image_at_resolution(resolution)
        else:
            return None

    def get_request(self, obj):
        """Returns the URL to the ArtRequest associated with this Image if
        one exists."""
        # check if the Image has both components for a GenericForeignKey
        if obj.content_type and obj.object_id:

            # get the model of the request type that the Image points to
            art_request_model = obj.content_type.model_class()

            # query for the object using the appropriate model type
            art_request_obj = art_request_model.objects.get(id=obj.object_id)

            # construct the URL name to reverse which matches Django Rest
            # Framework's generated pattern, a combination of namespace
            # (https://docs.djangoproject.com/en/1.8/topics/http/urls/#topics-http-reversing-url-namespaces),
            # content type model
            # (https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#the-contenttype-model),
            # and the view type, 'detail', which Django Rest Framework uses
            # to specify a detail view versus a list view
            # (http://www.django-rest-framework.org/api-guide/routers/#usage)
            detail_url = "v1:%s-detail" % obj.content_type.model

            # return the absolute url of the associated art request, using
            # Django Rest Framework's own reverse() function
            # (http://www.django-rest-framework.org/api-guide/reverse/#reverse)
            return reverse(detail_url, kwargs={'pk': art_request_obj.pk},
                           request=self.context['request'])

        else: # this Image isn't linked to a request
            return None


class VideoSerializer(MediaSerializer):
    class Meta:
        model = models.Video


class AudioSerializer(MediaSerializer):
    class Meta:
        model = models.Audio


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Review


class PollChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PollChoice


class PollSerializer(serializers.HyperlinkedModelSerializer):
    pollchoice_set = PollChoiceSerializer(many=True)
        # TODO: figure out how to change this field name to something nicer,
        # like "choices"

    class Meta:
        model = models.Poll
        fields = ('question', 'is_open', 'pollchoice_set')
