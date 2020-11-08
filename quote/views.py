from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import PowerPointProject, PowerPointQuote

def ppt_quote(request):
    projects = PowerPointProject.objects.all()

    template = 'quote/ppt_quote.html'
    context = {
        'projects': projects,
    }
    
    return render(request, template, context)
