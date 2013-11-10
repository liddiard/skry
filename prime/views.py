from prime.models import Issue, Article, PDF
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from dailybruin.settings.base import MEDIA_URL, STATIC_URL

def getRecentIssues(issue_slug):
    if issue_slug is None:
        issue = Issue.objects.latest('release_date')
        recent_issues = Issue.objects.order_by('-release_date')[1:4]
    else:
        issue = get_object_or_404(Issue, slug=issue_slug)
        if issue == Issue.objects.latest('release_date'):
            recent_issues = Issue.objects.order_by('-release_date')[1:4]
        else:
            recent_issues = Issue.objects.order_by('-release_date')[0:3]
    return issue, recent_issues


class IssueView(View):
    def get(self, context, slug):
        issue, recent_issues = getRecentIssues(slug)
        articles = Article.objects.filter(issue=issue).order_by('position')
        pdf = PDF.objects.get(issue=issue)
        context = {'issue': issue, 'recent_issues': recent_issues,
                   'articles': articles, 'pdf': pdf, 'MEDIA_URL': MEDIA_URL,
                   'STATIC_URL': STATIC_URL}
        return render_to_response('prime_front.html', context)

class ArticleView(View):
    def get(self, context, issue_slug, article_slug):
        issue, recent_issues = getRecentIssues(issue_slug)
        try:
            article = Article.objects.filter(issue=issue).get(slug=article_slug)
        except Article.DoesNotExist:
            raise Http404
        articles = Article.objects.filter(issue=issue).order_by('position')
        pdf = PDF.objects.get(issue=issue)
        context = {'issue': issue, 'recent_issues': recent_issues,
                   'article': article, 'articles': articles, 'pdf': pdf,
                   'MEDIA_URL': MEDIA_URL, 'STATIC_URL': STATIC_URL}
        return render_to_response('prime_article.html', context)
