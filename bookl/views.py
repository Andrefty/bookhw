from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book,Author
from .forms import BookForm,AuthorForm

# Create your views here.
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class BookListView(ListView):
    model = Book
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('bookl:book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('bookl:book_list')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('bookl:book_list')
    
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('bookl:book_list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('bookl:book_list')

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('bookl:book_list')