from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import PowerPointProject
from .forms import PowerPointProjectForm
from django.contrib.auth.models import User


def ppt_quote(request):
    projects = PowerPointProject.objects.all()

    if request.method == 'POST':
        form = PowerPointProjectForm(request.POST)
        if form.is_valid():

            # Getting the quote
            '''
            Check the value selected by users.
            If selection is 0,1 or both, increment by 5 to the quote.
            If selection is any of 2-5 or all, increment by 4.
            If selection is any of 6-8 or all, increment by 8.
            '''
            requirement = form['requirements'].value()
            quote = 0
            if '0' in requirement:
                quote += 5
            if '1' in requirement:
                quote += 5

            if '2' in requirement:
                quote += 4
            if '3' in requirement:
                quote += 4
            if '4' in requirement:
                quote += 4
            if '5' in requirement:
                quote += 4

            if '6' in requirement:
                quote += 8
            if '7' in requirement:
                quote += 8
            if '8' in requirement:
                quote += 8

            form.instance.quote = quote

            projects = form.save()
            messages.success(request, 'Successfully submitted for quote!')
            return redirect(reverse('ppt_quote_out'))
        else:
            messages.error(request, 'Failed to get quote. Please ensure the form is valid.')
    else:
        form = PowerPointProjectForm()

    template = 'quote/ppt_quote.html'
    context = {
        'projects': projects,
        'form': form,
    }

    return render(request, template, context)

def ppt_quote_out(request):
    # Page to show first 5 quotes received
    projects = PowerPointProject.objects.all().order_by('-date')[0:5]

    template = 'quote/ppt_quote_out.html'
    context = {
        'projects': projects,
    }
    return render(request, template, context)


def ppt_quote_detail(request, project_id):
    # Page to show the quote to the client
    quote = get_object_or_404(PowerPointProject, pk=project_id)

    # Getting the value text in requirements intead of key to render to html
    '''
    For key, value in requirements array,
    check if selected requirements' key is equal to
    key in requirements array. 
    If yes, append the value to the empty list quote_choices.
    '''
    quote_choices = []
    for k, v in quote.requirements.choices.items():
        for i in quote.requirements:
            if int(k) == int(i):
                quote_choices.append(v)

    template = 'quote/ppt_quote_detail.html'
    context = {
        'quote': quote,
        'quote_choices': quote_choices,
    }
    return render(request, template, context)


def web_quote(request):
    template = 'quote/web_quote.html'
    context = {

    }

    return render(request, template, context)
