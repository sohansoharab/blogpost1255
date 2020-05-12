from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Blog.models import Post

# Create your views here.


class HomePage(ListView):
    model = Post
    template_name = 'Blog/home.html'
    context_object_name = 'all_post'


class PostDetails(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'
    context_object_name = 'main_post'
