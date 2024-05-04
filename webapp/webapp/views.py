from django.shortcuts import render


def home(request):
    return render(request, './templates/home.html')


def about_me(request):
    return render(request, 'about.html')


def portfolio_projects(request):
    return render(request, 'portfolio_projects.html')


def contact_me(request):
    return render(request, 'contact.html')
