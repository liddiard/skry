from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Album

class MainView(TemplateView):

    template_name = 'music/front.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.all()

        return context

