from itertools import chain

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

from .models import Post, Project


class FrontView(TemplateView):

    template_name = "research/front.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:10]
        context['posts'] = Post.objects.all()[:10]
        return context


class PostsView(ListView):

    template_name = "research/posts.html"
    model = Post


class ProjectsView(ListView):

    template_name = "research/projects.html"
    model = Project


class PostView(DetailView):

    template_name = "research/post.html"
    model = Post


class ProjectView(DetailView):

    template_name = "research/project.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(project=model)
        return context
