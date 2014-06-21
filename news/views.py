import json
import datetime

from django.views.generic.base import View, TemplateView
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, RequestContext 
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.conf import settings
from django.db import transaction
from django.core import urlresolvers

from . import models


class CategoryView(TemplateView):

    template_name = "news/list.html"
    
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_slug = self.kwargs.get('category')
        all_articles = models.get_published_articles()
        context['other_categories'] = models.Category.objects\
                                            .filter(parent=None)\
                                            .exclude(slug=category_slug)
        if category_slug:
            category = get_object_or_404(models.Category, slug=category_slug)
            context['category'] = category
            context['articles'] = all_articles.filter(category=category)[:6]
        else:
            context['articles'] = all_articles[:6]
        return context


class TagView(TemplateView):
    pass


class ArticleView(CategoryView):
    
    template_name = "news/list.html"

    def get(self, request, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        # if an id paramater was passed, we'll look up the article with that
        if kwargs.get('id'):
            article = get_object_or_404(models.Article, id=kwargs.get('id')) 
        else: # otherwise we'll look it up with the pretty url scheme
            article = get_object_or_404(models.Article, 
                                        publish_time__year=kwargs.get('year'),
                                        publish_time__month=kwargs.get('month'),
                                        publish_time__day=kwargs.get('day'), 
                                        url_slug=kwargs.get('slug'))
        context['article'] = article
        if request.GET.get('format') == "json":
            if article.alternate_template:
                template_name = article.alternate_template.filename
            else:
                template_name = "news/inc/article.html"
            template = get_template(template_name)
            context = Context({'article': article, 
                               'STATIC_URL': settings.STATIC_URL, 
                               'MEDIA_URL': settings.MEDIA_URL})
            html = template.render(context)
            response_dict = {'pk': article.pk, 'html': html}
            response_json = json.dumps(response_dict)
            return HttpResponse(response_json, 
                                content_type="application/json")
        else:
            template_name = "news/list.html"
            return render_to_response(template_name, context, 
                                      context_instance=RequestContext(request))


class PageView(TemplateView):
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


class SubcategoriesJSONView(AjaxView):

    def get(self, request):
        category_slug = request.GET.get('category')
        try:
            category = models.Category.objects.get(slug=category_slug)
        except models.Category.DoesNotExist:
            return self.does_not_exist('Category matching slug (%s) does not '
                                       'exist.' % category_slug)
        subcategories = category.category_set.all()
        response_list = []
        for subcategory in subcategories:
            s = {}
            s['name'] = subcategory.name
            s['url'] = urlresolvers.reverse('news_category', 
                                            kwargs={'category': 
                                            subcategory.slug})
            s['slug'] = subcategory.slug
            response_list.append(s)
        return self.success(subcategories=response_list)


class CardsJSONView(AjaxView):
    
    def get(self, request):
        MAX_QUANTITY = 50
        start_after = request.GET.get('start_after')
        quantity = request.GET.get('quantity')
        if not quantity:
            return self.key_error('Required key (quantity) missing from '
                                  'request.')
        category = request.GET.get('category')
        try:
            quantity = int(quantity)
        except ValueError:
            return self.key_error('quantity %s is not an integer.' % quantity)
        # All requested articles are loaded into memory, so we don't want
        # a malicious user to be able to craft a request for more than a 
        # reasonable quantity and crash the application.
        if quantity > MAX_QUANTITY:
            return self.error(error='RangeError', message='Quantity requested '
                              'exceeds maximum allowed (%d).' % MAX_QUANTITY)
        articles = models.get_published_articles()
        if start_after:
            articles = articles.filter(position__lt=start_after)
        if category:
            try:
                c = models.Category.objects.get(slug=category)
            except models.Category.DoesNotExist:
                return self.does_not_exist('Category matching slug (%s) does '
                                           'not exist.' % category)
            articles = articles.filter(category=c)
        try:
            articles = articles[:quantity]
        except AssertionError:
            return self.error(error='AssertionError', message='quantity (%d) '
                              'is invalid.' % quantity)
        response_list = []
        for a in articles:
            response_list.append(a.card_html())
        return self.success(cards=response_list)


class RelatedArticlesView(AjaxView):
    pass


class ArticlePositionChangeView(AuthenticatedAjaxView):

    def post(self, request):
        article_id = request.POST.get('id')
        new_position = request.POST.get('new_position')
        if not article_id:
            return self.key_error('Required key (id) missing from request.')
        if not new_position:
            return self.key_error('Required key (new_position) missing from '
                                  'request.')
        try:
            new_position = int(new_position) # str to int for later comparison
        except ValueError:
            return self.key_error('new_positon (%s) is not an integer.'\
                                  % new_position)
        try:
            article = models.Article.objects.get(pk=article_id)
        except models.Article.DoesNotExist:
            return self.does_not_exist('Article matching id (%s) was not found.'\
                                        % article_id)
        current_position = article.position
        # (bool) will the displaced adjacent articles be shifted higher in
        # position or lower?
        shift_higher = new_position < current_position
        if shift_higher:
            pos1 = new_position
            pos2 = current_position
            order = '-position'
        else:
            pos1 = current_position
            pos2 = new_position
            order = 'position'
        articles_to_shift = models.Article.objects\
                                  .filter(position__range=(pos1, pos2))\
                                  .exclude(position=current_position)\
                                  .order_by(order)
        print articles_to_shift, shift_higher
        highest_position = models.Article.objects.first().position
        with transaction.atomic():
            # move the article to be rearranged to a temporary holding position, 
            # freeing up its position for another article to shift into
            article.position = highest_position + 1
            article.save()
            for a in articles_to_shift:
                if shift_higher:
                    a.position += 1
                else:
                    a.position -= 1
                a.save()
            article.position = new_position
            article.save()
        return self.success(card=article.pk, new_position=article.position)
