from django.contrib import admin
from blog.models import BlogPost
# Register your models here.
@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title',)

