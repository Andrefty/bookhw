from tabnanny import verbose
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name="Book author", max_length=100, unique=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name="Book name", max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publisher = models.CharField(verbose_name="Book publisher", max_length=100)
    pgnumber = models.IntegerField(verbose_name="Book pages")
    photo=models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name
