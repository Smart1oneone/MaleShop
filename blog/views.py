from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blogposts'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    context_object_name = 'blogpost'