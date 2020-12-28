from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    bookauthor = models.CharField(max_length=200)
    bookrejting = models.IntegerField()
    body = models.TextField()
    author = models.ForeignKey(
        'users.Store', # дефолтынй пользователь из django.contrib.auth
        on_delete = models.CASCADE,
    )


    def __str__(self):
        return self.title 