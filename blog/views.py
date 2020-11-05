from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import CommentForm, BlogForm

def blogs(request):
    blog_list = Blog.objects.all()
    query = None
    latest = Blog.objects.order_by('-date')[0:3]

    # Search in blog
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.info(request, "You can enter a keywords to use this search functionality")
                return redirect(reverse('blogs'))

            queries = Q(title__icontains=query) | Q(content__icontains=query)
            blog_list = blog_list.filter(queries)

    # Pagination 
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
        return redirect(reverse('blog_detail', args=[blog.id]))
    
    template = 'blog/blog_detail.html'

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, template, context)

@login_required
def add_blog(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has the permission to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST or None)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context ={
        'form': form,
    }

    return render(request, template, context)