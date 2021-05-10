from django.db import models
from admin_user.models import members, books

class transactions(models.Model):
    member = models.ForeignKey(members, on_delete=models.CASCADE)
    borrow_date = models.DateField()

class detail_transactions(models.Model):
    transaction = models.ForeignKey(transactions, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    is_returned = models.CharField(max_length=1)
    return_of_date = models.DateField(null=True)
    is_ontime = models.CharField(max_length=1, null=True)
