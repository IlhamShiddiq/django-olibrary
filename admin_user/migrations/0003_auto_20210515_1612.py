# Generated by Django 3.1.7 on 2021-05-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0002_auto_20210510_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
    ]
