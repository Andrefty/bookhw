# Generated by Django 4.1.2 on 2022-10-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookl', '0004_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
