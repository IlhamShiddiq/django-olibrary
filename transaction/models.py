from django.db import models
from admin_user.models import members, books
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

class transactions(models.Model):
    member = models.ForeignKey(members, on_delete=models.CASCADE)
    borrow_date = models.DateField()

class detail_transactions(models.Model):
    transaction = models.ForeignKey(transactions, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    is_returned = models.CharField(max_length=1)
    return_of_date = models.DateField(null=True)
    is_ontime = models.CharField(max_length=1, null=True)

    def __str__(self):
        return str(self.book_id)

@receiver(post_save, sender=detail_transactions)
def updating_stock(sender, instance, created, **kwargs):
    if created:
        update = books.objects.filter(id=instance.book_id).update(stock=F("stock") - 1)
    else:
        update = books.objects.filter(id=instance.book_id).update(stock=F("stock") + 1)