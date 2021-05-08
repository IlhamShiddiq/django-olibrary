from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url=settings.LOGIN_URL)
def book(request):
    return render(request, 'book-datas.html')

@login_required(login_url=settings.LOGIN_URL)
def publisher(request):
    return render(request, 'publisher.html')

@login_required(login_url=settings.LOGIN_URL)
def category(request):
    return render(request, 'category.html')

@login_required(login_url=settings.LOGIN_URL)
def transaction(request):
    return render(request, 'transaction.html')

@login_required(login_url=settings.LOGIN_URL)
def report(request):
    return render(request, 'report.html')
