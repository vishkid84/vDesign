from django.shortcuts import render
from .models import Contact


def contact(request):
    template = 'contact/contact.html'
    context = {

    }

    return render(request, template, context)