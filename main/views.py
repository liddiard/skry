from django.views.generic.base import View, TemplateView

from main.models import Author


class FrontView(TemplateView):
    pass


class CategoryView(TemplateView):
    pass


class ArticleView(TemplateView):
    pass


class PageView(TemplateView):
    pass


class RelatedArticlesView(View):
    pass
