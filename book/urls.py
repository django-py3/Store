from django.urls import path 
from .views import BookListView, BookDetailView, BookListViewAsc, BookListViewDesc

urlpatterns = [
    path("book/<int:pk>/", BookDetailView.as_view(), name="detail_book"),
    path("", BookListView.as_view(), name="books"),
    path("books_reversed_asc", BookListViewAsc.as_view(), name="books_reversed_asc"),
    path("books_reversed_desc", BookListViewDesc.as_view(), name="books_reversed_desc"),
]