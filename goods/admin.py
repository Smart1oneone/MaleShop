from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MaleClothes

@admin.register(MaleClothes)
class MaleClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'size', 'color', 'price', 'stock')
    search_fields = ('name', 'category', 'size', 'color')
    list_filter = ('category', 'size', 'color')