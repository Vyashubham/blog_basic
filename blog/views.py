from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Post, VyasProfile
from django.views.generic import ListView, DetailView

# Create your views here.

def home(requests):

    return render(requests, 'blog/index.html')

def profile(requests):

    return HttpResponse('profile')

def blog(requests):

    return HttpResponse('blog')


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-Date']

    paginate_by = 2 #change this to a higher number

class BlogpostListView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    context_object_name = 'posts'
    ordering = ['-Date']

    paginate_by = 2 #change this to a higher number


class PostDetailView(DetailView):
    model = Post


def profile(request):
    context = {

        'things': VyasProfile.objects.all()
    }

    return render(request, 'blog/profile.html', context)
