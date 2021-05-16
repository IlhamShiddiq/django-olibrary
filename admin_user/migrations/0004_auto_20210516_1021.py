# Generated by Django 3.1.7 on 2021-05-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0003_auto_20210515_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='publishers',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, default='book-default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]