import django_filters
from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    filter_fields = ('credit', 'request_type', 'request_id')
    search_fields = ('file', 'caption')
    ordering_fields = "__all__"


class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    filter_fields = ('credit',)
    search_fields = ('title', 'youtube_id')
    ordering_fields = "__all__"


class AudioViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Audio.objects.all()
    serializer_class = serializers.AudioSerializer
    filter_fields = ('credit',)
    search_fields = ('title', 'file')
    ordering_fields = "__all__"


class ReviewFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter(name='rating', lookup_type='gte')
    max_rating = django_filters.NumberFilter(name='rating', lookup_type='lte')

    class Meta:
        model = models.Review
        fields = ['rating', 'min_rating', 'max_rating']


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_class = ReviewFilter
    search_fields = ('item', 'line_1', 'line_2')
    ordering_fields = "__all__"


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    filter_fields = ('is_open',)
    search_fields = ('question',)
    ordering_fields = "__all__"


class PollChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.PollChoice.objects.all()
    serializer_class = serializers.PollChoiceSerializer
    filter_fields = ('question', 'votes')
    search_fields = ('text',)
    ordering_fields = "__all__"
