from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from transaction.models import *
from admin_user.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

@login_required()
def transaction(request):
    try:
        del request.session['member_datas']
        del request.session['book_regs']
    except:
        a = 'nothing'

    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    transaction_datas = transactions.objects.raw('SELECT t.id, name, count(d.book_id) AS count FROM transaction_transactions t, transaction_detail_transactions d, admin_user_books b, admin_user_members m WHERE t.id=d.transaction_id AND d.book_id = b.id AND t.member_id=m.id and d.is_returned="0" GROUP BY t.id')
    paginator = Paginator(transaction_datas, 5)

    page_number = request.GET.get('page')
    transaction_paginate = paginator.get_page(page_number)

    datas = {
        'transactions': transaction_paginate,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'transaction/transaction.html', datas)

@login_required()
def member_validation(request):
    if request.POST:
        email = request.POST.get('email')
        try:
            validation = members.objects.get(email=email)

            request.session['member_datas'] = [validation.id, validation.name]
            # del request.session['member_datas']

            return redirect('add_transaction')
        except members.DoesNotExist:
            messages.error(request, 'Sorry, email is not registered in our system')
            return redirect('transaction')
            
@login_required()
def submit_transaction(request):
    if request.POST:
        member = request.session.get('member_datas')
        entry = request.session.get('book_regs')

        if entry == None:
            del request.session['member_datas']

            messages.error(request, 'You don\'t have any entries')
            return redirect('transaction')

        current_date = datetime.datetime.now().date()  
        member_datas = members.objects.get(id=member[0])
        book_amount = entry.count('~')
        book_isbn = entry.split('~')[:book_amount]

        create_transaction = transactions.objects.create(
            borrow_date=current_date,
            member_id=member[0]
        )

        for i in range(0, book_amount):
            book_data = books.objects.get(isbn=book_isbn[i])
            create_d_transaction = detail_transactions.objects.create(
                is_returned='0',
                return_of_date='0001-01-01',
                is_ontime='',
                book_id=book_data.id,
                transaction_id=create_transaction.id
            )

        messages.success(request, 'Transaction has added successfully')
        return redirect('transaction')


@login_required()
def add_transaction(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    data = request.session.get('member_datas')

    if data == None:
        messages.error(request, 'You don\'t have member data')
        return redirect('transaction')

    status = ''
    sendmessage = ''
    entries = []

    if request.POST:
        isbn = request.POST.get('isbn')
        try:
            # Checking book data from ISBN 
            validation = books.objects.get(isbn=isbn)

            try:
                book_reg = request.session['book_regs']

                # Checking the entries is already have 2 or not
                if book_reg.count('~') == 2:
                    status = 'failed'
                    sendmessage = 'Sorry, you already have 2 books in your entry'
                else:
                    get_book_reg = book_reg.split('~')
                    if get_book_reg[0] == isbn:
                        status = 'failed'
                        sendmessage = 'Sorry, member can\'t borrow the same book'
                    else:
                        if validation.stock == 0:
                            status = 'failed'
                            sendmessage = 'Sorry, this book is unavailable'
                        else:
                            request.session['book_regs'] += isbn + '~'
                            status = 'success'
                            sendmessage = 'Book has added successfully to your entry'
            except:
                if validation.stock == 0:
                    status = 'failed'
                    sendmessage = 'Sorry, this book is unavailable'
                else:
                    book_reg = request.session['book_regs'] = isbn + '~'

                    status = 'success'
                    sendmessage = 'Book has added successfully to your entry'
        except books.DoesNotExist:
            status = 'failed'
            sendmessage = 'Sorry, ISBN Code is not registered in our system'

    try:
        book_regs = request.session['book_regs']
        isbns = book_regs.split('~')[:book_regs.count('~')]
        for i in range(0, book_regs.count('~')) :
            book = books.objects.get(isbn=isbns[i])
            entries.append(book.title)  
    except:
        entries.append('-')

    datas = {
        'memberdata': {
            'id': data[0],
            'name': data[1]
        },
        'status': status,
        'sendmessage': sendmessage,
        'entries': entries,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'transaction/add-transaction.html', datas)

@login_required()
def cancel_transaction(request):
    try:
        del request.session['book_regs']
        del request.session['member_datas']
    except:
        del request.session['member_datas']

    messages.success(request, 'Transaction is canceled')
    return redirect('transaction')

@login_required()
def returning(request, transaction_id):
    message = ''
    is_ontime = '1'
    current_date = datetime.datetime.now().date()
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()

    if request.POST:
        book_lists = request.POST.getlist('book')
        id = request.POST.get('id')

        transaction_data = transactions.objects.get(id=id)
        interval_borrow_date = transaction_data.borrow_date + datetime.timedelta(days=14)

        if interval_borrow_date < current_date:
            is_ontime = '0'

        for i in range(0, len(book_lists)):
            detail = detail_transactions.objects.get(transaction_id=id, book_id=book_lists[i])
            detail.is_returned = '1'
            detail.return_of_date = current_date
            detail.is_ontime = is_ontime
            detail.save()
            
        if len(book_lists) == 1:
            message = 'The book is returned'
        else :
            message = 'The books are returned'

        messages.success(request, message)
        return redirect('transaction')

    transaction_data = transactions.objects.get(id=transaction_id)
    book_datas = detail_transactions.objects.raw('SELECT d.id AS id, b.id AS id_b, b.title AS title FROM transaction_detail_transactions d, admin_user_books b WHERE d.book_id=b.id AND d.transaction_id='+str(transaction_id)+' AND d.is_returned="0"')

    datas = {
        'transaction': transaction_data,
        'books': book_datas,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'transaction/return.html', datas)

@login_required()
def report(request):
    book_count = books.objects.all().count()
    publisher_count = publishers.objects.all().count()
    category_count = categories.objects.all().count()
    report = transactions.objects.raw('SELECT t.id AS id, m.name AS name, b.title AS title, d.return_of_date AS return_date, d.is_ontime AS ontime FROM transaction_transactions t, transaction_detail_transactions d, admin_user_books b, admin_user_members m WHERE t.id=d.transaction_id AND d.book_id = b.id AND t.member_id=m.id and d.is_returned="1"')
    paginator = Paginator(report, 5)

    page_number = request.GET.get('page')
    report_paginate = paginator.get_page(page_number)

    datas = {
        'reports': report_paginate,
        'book_count': book_count,
        'publisher_count': publisher_count,
        'category_count': category_count,
    }

    return render(request, 'report/report.html', datas)

