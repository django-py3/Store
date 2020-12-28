from django.views.generic import ListView, DetailView 
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book 
    template_name = "book.html"
    context_object_name = "books"

class BookListViewAsc(ListView):
    model = Book 
    template_name = "book.html"
    context_object_name = "books"
    ordering = ['bookrejting']

class BookListViewDesc(ListView):
    model = Book 
    template_name = "book.html"
    context_object_name = "books"
    ordering = ['-bookrejting']
    

class BookDetailView(DetailView):
    model = Book 
    template_name = "detail_book.html"
    context_object_name = "book"