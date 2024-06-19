from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import MaleClothes

class HomePageView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['products'] = MaleClothes.objects.all()
        return context