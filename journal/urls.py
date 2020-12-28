from django.urls import path 
from .views import JournalListView, JournalDetailView, JournalListViewAsc,  JournalListViewDesc

urlpatterns = [
    path("journal/<int:pk>/", JournalDetailView.as_view(), name="detail_journal"),
    path("", JournalListView.as_view(), name="journals"),
    path("journals_reversed_asc", JournalListViewAsc.as_view(), name="journals_reversed_asc"),
    path("journals_reversed_desc", JournalListViewDesc.as_view(), name="journals_reversed_desc"),
]