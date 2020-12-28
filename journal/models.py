from django.db import models

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=250)
    journalauthor = models.CharField(max_length=200)
    journalspagecount = models.IntegerField()
    body = models.TextField()
    author = models.ForeignKey(
        'users.Store', # дефолтынй пользователь из django.contrib.auth
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.title 
