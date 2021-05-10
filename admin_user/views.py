from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url=settings.LOGIN_URL)
def book(request):
    return render(request, 'book/book-datas.html')

@login_required(login_url=settings.LOGIN_URL)
def add_book(request):
    return render(request, 'book/add-book.html')

@login_required(login_url=settings.LOGIN_URL)
def edit_book(request):
    return render(request, 'book/edit-book.html')

@login_required(login_url=settings.LOGIN_URL)
def detail_book(request):
    return render(request, 'book/detail-book.html')

@login_required(login_url=settings.LOGIN_URL)
def member(request):
    return render(request, 'member/member.html')

@login_required(login_url=settings.LOGIN_URL)
def publisher(request):
    return render(request, 'publisher/publisher.html')

@login_required(login_url=settings.LOGIN_URL)
def add_publisher(request):
    return render(request, 'publisher/add-publisher.html')

@login_required(login_url=settings.LOGIN_URL)
def edit_publisher(request):
    return render(request, 'publisher/edit-publisher.html')

@login_required(login_url=settings.LOGIN_URL)
def category(request):
    return render(request, 'category/category.html')

@login_required(login_url=settings.LOGIN_URL)
def add_category(request):
    return render(request, 'category/add-category.html')

@login_required(login_url=settings.LOGIN_URL)
def edit_category(request):
    return render(request, 'category/edit-category.html')

@login_required(login_url=settings.LOGIN_URL)
def transaction(request):
    return render(request, 'transaction.html')

@login_required(login_url=settings.LOGIN_URL)
def report(request):
    return render(request, 'report.html')
