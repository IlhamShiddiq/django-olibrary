from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from admin_user.form import *

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url=settings.LOGIN_URL)
def book(request):
    return render(request, 'book/book-datas.html')

@login_required(login_url=settings.LOGIN_URL)
def add_book(request):
    datas = {
        'form': FormBook(),
    }

    return render(request, 'book/add-book.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def edit_book(request):
    datas = {
        'form': FormBook(),
    }

    return render(request, 'book/edit-book.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def detail_book(request):
    return render(request, 'book/detail-book.html')

@login_required(login_url=settings.LOGIN_URL)
def member(request):
    return render(request, 'member/member.html')

@login_required(login_url=settings.LOGIN_URL)
def add_member(request):
    datas = {
        'form': FormMember(),
    }

    return render(request, 'member/add-member.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def edit_member(request):
    datas = {
        'form': FormMember(),
    }

    return render(request, 'member/edit-member.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def detail_member(request):
    return render(request, 'member/detail-member.html')

@login_required(login_url=settings.LOGIN_URL)
def publisher(request):
    return render(request, 'publisher/publisher.html')

@login_required(login_url=settings.LOGIN_URL)
def add_publisher(request):
    datas = {
        'form': FormPublisher(),
    }

    return render(request, 'publisher/add-publisher.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def edit_publisher(request):
    datas = {
        'form': FormPublisher(),
    }
    return render(request, 'publisher/edit-publisher.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def category(request):
    return render(request, 'category/category.html')

@login_required(login_url=settings.LOGIN_URL)
def add_category(request):
    datas = {
        'form': FormCategory(),
    }

    return render(request, 'category/add-category.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def edit_category(request):
    datas = {
        'form': FormCategory
    }

    return render(request, 'category/edit-category.html', datas)