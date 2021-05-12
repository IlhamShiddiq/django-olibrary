from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin_user.form import *
from admin_user.models import *

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required()
def book(request):
    book_lists = books.objects.all()

    datas = {
        'books': book_lists,
    }

    return render(request, 'book/book-datas.html', datas)

@login_required()
def add_book(request):
    if request.POST:
        data = FormBook(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has added successfully')
            return redirect('book')

        messages.error(request, 'Failed to add data')
        return redirect('book')

    datas = {          
        'form': FormBook(),
    }

    return render(request, 'book/add-book.html', datas)

@login_required()
def edit_book(request, book_id):
    book = books.objects.get(id=book_id)

    if request.POST:
        data = FormBook(request.POST, instance=book)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data has updated successfully')
            return redirect('book')

        messages.error(request, 'Failed to update data')
        return redirect('book')

    form = FormBook(instance=book)

    datas = {
        'form': form,
        'book': book
    }

    return render(request, 'book/edit-book.html', datas)

@login_required()
def detail_book(request, book_id):
    book = books.objects.get(id=book_id)

    datas = {
        'book': book
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
    member = members.objects.all()

    datas = {
        'members': member
    }

    return render(request, 'member/member.html', datas)

@login_required()
def add_member(request):
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
    }

    return render(request, 'member/add-member.html', datas)

@login_required()
def edit_member(request, member_id):
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
        'member': member
    }

    return render(request, 'member/edit-member.html', datas)

@login_required()
def detail_member(request, member_id):
    member = members.objects.get(id=member_id)

    datas = {
        'member': member
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
    publisher_lists = publishers.objects.all()

    datas = {
        'publishers': publisher_lists
    }

    return render(request, 'publisher/publisher.html', datas)

@login_required()
def add_publisher(request):
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
    }

    return render(request, 'publisher/add-publisher.html', datas)

@login_required()
def edit_publisher(request, publisher_id):
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
        'publisher': publisher
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
    category = categories.objects.all()

    datas = {
        'categories': category
    }

    return render(request, 'category/category.html', datas)

@login_required()
def add_category(request):
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
    }

    return render(request, 'category/add-category.html', datas)

@login_required()
def edit_category(request, category_id):
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
        'category': category
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