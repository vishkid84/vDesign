from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.contrib import messages

from .models import Blog
from .forms import CommentForm

def blogs(request):
    blog_list = Blog.objects.all()
    query = None
    latest = Blog.objects.order_by('-date')[0:3]

    # Search in blog
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.info(request, "Enter keywords to search")
                return redirect(reverse('blogs'))

            queries = Q(title__icontains=query) | Q(content__icontains=query)
            blog_list = blog_list.filter(queries)


    paginator =Paginator(blog_list, 3)
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
        'search': query,
    }
    return render(request, template, context)


def blog_detail(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.blog = blog
            form.save()
    
    template = 'blog/blog_detail.html'

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, template, context)