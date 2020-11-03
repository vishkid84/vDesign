from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogs(request):
    blog_list = Blog.objects.all()
    latest = Blog.objects.order_by('-date')[0:3]
    template = 'blog/blogs.html'
    context = {
        'blog_list': blog_list,
        'latest': latest,
    }
    return render(request, template, context)