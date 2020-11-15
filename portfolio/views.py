from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def portfolios(request):
    portfolios = Portfolio.objects.all()

    template = 'portfolio/portfolios.html'
    context = {
        'portfolios': portfolios,
    }

    return render(request, template, context)
