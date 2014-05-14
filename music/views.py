from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Album

class MainView(TemplateView):

    template_name = 'music/front.html'

    def getContextData(self, context):
        pass
