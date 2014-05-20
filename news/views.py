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


class AjaxView(View):

    def json_response(self, **kwargs):
    return HttpResponse(json.dumps(kwargs), content_type="application/json")

    def success(self, **kwargs):
    return self.json_response(result=0, **kwargs)

    def error(self, error, message):
    return self.json_response(result=1, error=error, message=message)

    def authentication_error(self):
    return self.error("AuthenticationError", "User is not authenticated.")

    def access_error(self, message):
    return self.error("AccessError", message)

    def key_error(self, message):
    return self.error("KeyError", message)

    def does_not_exist(self, message):
    return self.error("DoesNotExist", message)

    def validation_error(self, message):
    return self.error("ValidationError", message)


class AuthenticatedAjaxView(AjaxView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(AuthenticatedAjaxView, self).dispatch(request, *args,
                         **kwargs)
        else:
            return self.authentication_error()
