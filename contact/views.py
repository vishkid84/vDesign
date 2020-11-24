from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid:
            contact = form.save()
            messages.success(request, 'Successfully sent your message!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
