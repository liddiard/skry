from rest_framework import viewsets

from . import serializers
from . import models


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    filter_fields = ('credit', 'request_type', 'request_id')
    search_fields = ('file', 'caption')
    ordering_fields = "__all__"


class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    filter_fields = ('credit',)
    search_fields = ('title', 'youtube_id')
    ordering_fields = "__all__"


class AudioViewSet(viewsets.ModelViewSet):
    queryset = models.Audio.objects.all()
    serializer_class = serializers.AudioSerializer
    filter_fields = ('credit',)
    search_fields = ('title', 'file')
    ordering_fields = "__all__"


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_fields = ('rating',)
    search_fields = ('item', 'line_1', 'line_2')
    ordering_fields = "__all__"


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    filter_fields = ('is_open',)
    search_fields = ('question',)
    ordering_fields = "__all__"


class PollChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.PollChoice.objects.all()
    serializer_class = serializers.PollChoiceSerializer
    filter_fields = ('question', 'votes')
    search_fields = ('text',)
    ordering_fields = "__all__"
