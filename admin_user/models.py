from django.db import models

class publishers(models.Model):
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.publisher

class categories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class books(models.Model):
    isbn = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    stock = models.IntegerField()
    writer = models.CharField(max_length=100)
    publisher = models.ForeignKey(publishers, on_delete=models.CASCADE)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    synopsis = models.TextField()
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class members(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name