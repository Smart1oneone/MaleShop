from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import MaleClothes

class GoodsView(TemplateView):
    template_name = 'goods/goods.html'

    # def get(self, request, *args, **kwargs):
    #     category_slug = kwargs.get('category_slug')
    #     context = {
    #         'category_slug': category_slug,
    #     }
    #     return render(request, 'goods/goods.html', context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        category_slug = context['category_slug']
        if category_slug == None:
            context['products'] = MaleClothes.objects.all()
        if category_slug:
            context['products'] = MaleClothes.objects.filter(category=category_slug)
        return context

class ProductsView(TemplateView):
    pass