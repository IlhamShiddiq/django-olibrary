from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def transaction(request):
    return render(request, 'transaction/transaction.html')

@login_required(login_url=settings.LOGIN_URL)
def report(request):
    return render(request, 'report/report.html')

