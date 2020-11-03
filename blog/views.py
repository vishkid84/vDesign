from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Blog

# Create your views here.
def blogs(request):
    blog_list = Blog.objects.all()
    latest = Blog.objects.order_by('-date')[0:3]

    paginator =Paginator(blog_list, 1)
    page = request.GET.get('page', 1)

    try:
        number_of_blogs = paginator.page(page)
    except PageNotAnInteger:
        number_of_blogs = paginator.page(1)
    except EmptyPage:
        number_of_blogs = paginator.page(paginator.num_pages)

    template = 'blog/blogs.html'
    context = {
        'number_of_blogs': number_of_blogs,
        'latest': latest,
        'blog_list': number_of_blogs,
    }
    return render(request, template, context)