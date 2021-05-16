from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
import os

class publishers(models.Model):
    class Meta:
        ordering = ['id']

    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.publisher

class categories(models.Model):
    class Meta:
        ordering = ['id']

    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'book-cover/{0}/{1}'.format(instance.isbn, filename)

class books(models.Model):
    class Meta:
        ordering = ['id']
        
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    stock = models.IntegerField()
    writer = models.CharField(max_length=100)
    publisher = models.ForeignKey(publishers, on_delete=models.CASCADE)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    synopsis = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='book-cover/book-default.png', null=True, blank=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=books)
def delete_dir_image(sender, instance, *args, **kwargs):
    instance.image.delete(save=False)
    if instance.image != 'book-cover/book-default.png':
        os.rmdir(os.path.join(settings.MEDIA_URL_BOOK, instance.isbn))

@receiver(pre_save, sender=books)
def delete_while_update(sender, instance, *args, **kwargs):
    if instance.image != 'book-cover/book-default.png':
        try:
            old_img = instance.__class__.objects.get(id=instance.id).image.path
            try:
                new_img = instance.image.path
            except:
                new_img = None
            if new_img != old_img:
                if os.path.exists(old_img):
                    os.remove(old_img)
        except:
            pass

class members(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to='cover/', null=True)

    def __str__(self):
        return self.name