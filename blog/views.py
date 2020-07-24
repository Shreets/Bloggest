from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog
from django.core.paginator import Paginator


class BlogView(ListView):
    template_name = 'blog/blog.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 2


class DetailView(DetailView):
    model = Blog
    template_name = 'blog/details.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'blog'
