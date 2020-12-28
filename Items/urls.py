# articles/urls.py
from django.urls import path 

from .views import ItemsListView, ItemDetailView, ItemUpdateView, ItemDeleteView, ItemCreateView

urlpatterns = [
    path("<int:pk>/", ItemDetailView.as_view(), name="detail_item"), # articles/3/
    path("<int:pk>/edit/", ItemUpdateView.as_view(), name= "edit_item"), # articles/2/update/
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name= "delete_item"),
    path("new/", ItemCreateView.as_view(), name="new_item"),
    path("", ItemsListView.as_view(), name="items"),
]