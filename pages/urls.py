from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path("page/<int:pk>/delete/", PageDeleteView.as_view(), name = "delete_page"),
    path("page/<int:pk>/update/", PageUpdateView.as_view(), name="update_page"),

    path("page/new/", PageCreateView.as_view(), name = "new_page"),
    path("page/<int:pk>/", PageDetailView.as_view(), name="detail_page"),
    path("", PageListView.as_view(), name="home"),
]
