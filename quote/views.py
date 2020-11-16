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
            Check if low, medium or high values appear in the requirement input form.
            Count the number of occurences in each.
            Multiply them by individual price rate set for high, medium and low
            '''
            req = form['requirements'].value()
            if 'Low' in req:
                low = req.count('Low')
                low_quote = 5 * low
            else:
                low_quote = 0
            print (low_quote)

            if 'Medium' in req:
                medium = req.count('Medium')
                medium_quote = 4 * medium
            else:
                medium_quote = 0
            print (medium_quote)

            if 'High' in req:
                high = req.count('High')
                high_quote = 8 * high
            else:
                high_quote = 0
            print (high_quote)

            form.instance.quote = low_quote + medium_quote + high_quote

            projects = form.save()
            messages.success(request, 'Successfully submitted for quote!')
            return redirect(reverse('ppt_quote_out'))
        else:
            messages.error(request, 'Failed to get quote. Please ensure the form is valid.')
    else:
        form = PowerPointProjectForm()
        print (form.instance.requirements)

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

    template = 'quote/ppt_quote_detail.html'
    context = {
        'quote': quote,
    }
    return render(request, template, context)


def web_quote(request):
    template = 'quote/web_quote.html'
    context = {

    }

    return render(request, template, context)
