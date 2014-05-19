from django.views.generic.base import View, TemplateView
from django.shortcuts import get_object_or_404

from . import models
from . import utils


class FrontView(TemplateView):

    template_name = "news/list.html"

    def get_context_data(self):
        context = super(FrontView, self).get_context_data()
        context['articles'] = utils.get_published_articles()[:12]
        return context


class CategoryView(TemplateView):
    
    def get_context_data(self):
        context = super(CategoryView, self).get_context_data()
        category = self.kwargs.get('category')
        context['category'] = get_object_or_404(models.Category, 
                                                    slug=category)
        return context


class ArticleView(TemplateView):
    pass


class PageView(TemplateView):
    pass


class RelatedArticlesView(View):
    pass
