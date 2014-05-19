from django.utils.timezone import now as django_now

from . import models


def get_published_articles():
    return (models.Article.objects.filter(status=7)
            .filter(publish_time__lt=django_now()))
