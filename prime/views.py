from prime.models import Issue, Article
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response
from dailybruin.settings.base import MEDIA_URL

class Front(View):
    def get(self, context):
        current_issue = Issue.objects.latest('release_date')
        articles = Article.objects.filter(issue=current_issue)
        context = {'articles': articles, 'MEDIA_URL': MEDIA_URL}
        return render_to_response('prime_front.html', context)

class Article(DetailView):
    model = Article
    template_name = "prime_article.html"

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        # additional context vars here
        return context
