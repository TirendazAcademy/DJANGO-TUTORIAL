from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name = "post_yeni.html"
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields=['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_silme.html"
    success_url=reverse_lazy("home")


