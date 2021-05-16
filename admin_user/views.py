from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin_user.form import *
from admin_user.models import *
from transaction.models import *
from django.db.models import Count
from django.core.paginator import Paginator
import datetime
import os

@login_required()
def dashboard(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    theday = datetime.date.today()
    weekday = theday.isoweekday()
    dates = []

    top_publisher = books.objects.all().values('publisher_id', 'publisher_id__publisher').annotate(count=Count('publisher_id')).order_by('-count')[0:3]
    top_category = books.objects.all().values('category_id', 'category_id__category').annotate(count=Count('category_id')).order_by('-count')[0:3]

    start = theday - datetime.timedelta(days=weekday)
    date = [dates.append(start + datetime.timedelta(days=d)) for d in range(8)]

    monday = transactions.objects.filter(borrow_date=dates[1]).count()
    tuesday = transactions.objects.filter(borrow_date=dates[2]).count()
    wednesday = transactions.objects.filter(borrow_date=dates[3]).count()
    thursday = transactions.objects.filter(borrow_date=dates[4]).count()
    friday = transactions.objects.filter(borrow_date=dates[5]).count()

    datas = {
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
        'top_publisher_labels': [
            top_publisher[0]['publisher_id__publisher'],
            top_publisher[1]['publisher_id__publisher'],
            top_publisher[2]['publisher_id__publisher'],
        ],
        'top_publisher_counter': [
            top_publisher[0]['count'],
            top_publisher[1]['count'],
            top_publisher[2]['count'],
        ],
        'top_category_labels': [
            top_category[0]['category_id__category'],
            top_category[1]['category_id__category'],
            top_category[2]['category_id__category'],
        ],
        'top_category_counter': [
            top_category[0]['count'],
            top_category[1]['count'],
            top_category[2]['count'],
        ],
        'transaction_counter': [monday, tuesday, wednesday, thursday, friday]
    }

    return render(request, 'dashboard.html', datas)

@login_required()
def book(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    paginator = Paginator(books.objects.all(), 5)

    page_number = request.GET.get('page')
    book_lists = paginator.get_page(page_number)

    datas = {
        'books': book_lists,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'book/book-datas.html', datas)

@login_required()
def add_book(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()

    if request.POST:
        isbn = request.POST.get('isbn')
        data = FormBook(request.POST, request.FILES)
        if data.is_valid():
            data.save()

            messages.success(request, 'Data has added successfully')
            return redirect('book')

        messages.error(request, 'Failed to add data')
        return redirect('book')

    datas = {          
        'form': FormBook(),
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'book/add-book.html', datas)

@login_required()
def edit_book(request, book_id):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    book = books.objects.get(id=book_id)

    if request.POST:
        data = FormBook(request.POST, request.FILES, instance=book)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has updated successfully')
            return redirect('book')

        messages.error(request, 'Failed to update data')
        return redirect('book')

    form = FormBook(instance=book)

    datas = {
        'form': form,
        'book': book,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'book/edit-book.html', datas)

@login_required()
def detail_book(request, book_id):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    book = books.objects.get(id=book_id)

    datas = {
        'book': book,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'book/detail-book.html', datas)

@login_required()
def delete_book(request):
    if request.POST:
        id = request.POST.get('id')
        book = books.objects.get(id=id)

        delete = books.objects.filter(id=id).delete()

        messages.success(request, 'Data has deleted successfully')
        return redirect('book')

@login_required()
def member(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    paginator = Paginator(members.objects.all(), 5)

    page_number = request.GET.get('page')
    member = paginator.get_page(page_number)

    datas = {
        'members': member,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'member/member.html', datas)

@login_required()
def add_member(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()

    if request.POST:
        data = FormMember(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has added successfully')
            return redirect('member')

        messages.error(request, 'Failed to add data')
        return redirect('member')

    datas = {
        'form': FormMember(),
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'member/add-member.html', datas)

@login_required()
def edit_member(request, member_id):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    member = members.objects.get(id=member_id)

    if request.POST:
        data = FormMember(request.POST, instance=member)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has updated successfully')
            return redirect('member')

        messages.error(request, 'Failed to update data')
        return redirect('member')

    datas = {
        'form': FormMember(instance=member),
        'member': member,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'member/edit-member.html', datas)

@login_required()
def detail_member(request, member_id):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    member = members.objects.get(id=member_id)

    datas = {
        'member': member,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'member/detail-member.html', datas)
    
@login_required()
def delete_member(request):
    if request.POST:
        id = request.POST.get('id')
        category = members.objects.get(id=id)

        delete = members.objects.filter(id=id).delete()

        messages.success(request, 'Data has deleted successfully')
        return redirect('member')

@login_required()
def publisher(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    paginator = Paginator(publishers.objects.all(), 10)
    
    page_number = request.GET.get('page')
    publisher_lists = paginator.get_page(page_number)

    datas = {
        'publishers': publisher_lists,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'publisher/publisher.html', datas)

@login_required()
def add_publisher(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()

    if request.POST:
        data = FormPublisher(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has added successfully')
            return redirect('publisher')

        messages.error(request, 'Failed to add data')
        return redirect('publisher')
        
    datas = {
        'form': FormPublisher(),
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'publisher/add-publisher.html', datas)

@login_required()
def edit_publisher(request, publisher_id):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    publisher = publishers.objects.get(id=publisher_id)

    if request.POST:
        data = FormPublisher(request.POST, instance=publisher)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has updated successfully')
            return redirect('publisher')

        messages.error(request, 'Failed to update data')
        return redirect('publisher')

    datas = {
        'form': FormPublisher(instance=publisher),
        'publisher': publisher,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'publisher/edit-publisher.html', datas)

@login_required()
def delete_publisher(request):
    if request.POST:
        id = request.POST.get('id')
        publisher = publishers.objects.get(id=id)

        delete = publishers.objects.filter(id=id).delete()

        messages.success(request, 'Data has deleted successfully')
        return redirect('publisher')

@login_required()
def category(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    paginator = Paginator(categories.objects.all(), 10)

    page_number = request.GET.get('page')
    category = paginator.get_page(page_number)

    datas = {
        'categories': category,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'category/category.html', datas)

@login_required()
def add_category(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()

    if request.POST:
        data = FormCategory(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has added successfully')
            return redirect('category')

        messages.error(request, 'Failed to add data')
        return redirect('category')

    datas = {
        'form': FormCategory(),
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'category/add-category.html', datas)

@login_required()
def edit_category(request, category_id):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    category = categories.objects.get(id=category_id)
    
    if request.POST:
        data = FormCategory(request.POST, instance=category)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has updated successfully')
            return redirect('category')

        messages.error(request, 'Failed to update data')
        return redirect('category')

    datas = {
        'form': FormCategory(instance=category),
        'category': category,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'category/edit-category.html', datas)

@login_required()
def delete_category(request):
    if request.POST:
        id = request.POST.get('id')
        category = categories.objects.get(id=id)

        delete = categories.objects.filter(id=id).delete()

        messages.success(request, 'Data has deleted successfully')
        return redirect('category')