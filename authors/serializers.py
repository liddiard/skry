from rest_framework import serializers

from access import serializers as access_serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(AuthorSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated():
            self.fields['user'] = access_serializers.UserSerializer()
