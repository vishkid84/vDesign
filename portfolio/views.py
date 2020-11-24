from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Portfolio
from .forms import PortfolioForm


def portfolios(request):
    portfolios = Portfolio.objects.all().order_by('-date')

    template = 'portfolio/portfolios.html'
    context = {
        'portfolios': portfolios,
    }

    return render(request, template, context)


def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    template = 'portfolio/portfolio_detail.html'

    context = {
        'portfolio': portfolio,
    }

    return render(request, template, context)


@login_required
def add_portfolio(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has the permission to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save()
            messages.success(request, 'Successfully added portfolio item!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            messages.error(request, 'Failed to add portfolio item. Please ensure the form is valid.')
    else:
        form = PortfolioForm()

    template = 'portfolio/add_portfolio.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_portfolio(request, portfolio_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has the permission to do that.')
        return redirect(reverse('home'))

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save()
            messages.success(request, 'Successfully update portfolio!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            messages.error(request, 'Failed to add portfolio. Please ensure the form is valid.')
    else:
        form = PortfolioForm(instance=portfolio)
        messages.info(request, f'You are editing {portfolio.name}')

    template = 'portfolio/edit_portfolio.html'
    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, template, context)


@login_required
def delete_portfolio(request, portfolio_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has the permission to do that.')
        return redirect(reverse('home'))

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    portfolio.delete()
    messages.success(request, 'Portfolio item deleted')
    return redirect(reverse('portfolios'))
