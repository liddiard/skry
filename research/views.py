from itertools import chain

from django.views.generic.base import TemplateView
from django.core.paginator import Paginator

from .models import Post, Project


class FrontView(TemplateView):

    template_name = "research/front.html"
    ITEMS_PER_PAGE = 10

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:ITEMS_PER_PAGE]
        context['posts'] = Post.objects.all()[:ITEMS_PER_PAGE]
        return context


class PostsView(ListView):

    model = Post


class ProjectsView(ListView):

    model = Project


class PostView(DetailView):

    model = Post


class ProjectView(DetailView):

    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(project=model)
        return context
