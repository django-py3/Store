from django.contrib import admin
from .models import Journal
# Register your models here.

admin.site.register(Journal)
list_display = ["title", "author", "journalspagecount"]