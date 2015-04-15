from rest_framework import serializers

from . import models


class InternalCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InternalComment
