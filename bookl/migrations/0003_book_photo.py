# Generated by Django 4.1.2 on 2022-10-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookl', '0002_author_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, upload_to='upload/'),
        ),
    ]
