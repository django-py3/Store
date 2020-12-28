from django.views.generic import ListView, DetailView 
from .models import Journal

# Create your views here.

class JournalListView(ListView):
    model = Journal 
    template_name = "journal.html"
    context_object_name = "journals"

class JournalListViewAsc(ListView):
    model = Journal 
    template_name = "journal.html"
    context_object_name = "journals"
    ordering = ['journalspagecount']

class JournalListViewDesc(ListView):
    model = Journal 
    template_name = "journal.html"
    context_object_name = "journals"
    ordering = ['-journalspagecount']

class JournalDetailView(DetailView):
    model = Journal 
    template_name = "detail_journal.html"
    context_object_name = "journal"