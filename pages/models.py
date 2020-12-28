from django.db import models
from django.urls import reverse

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=250)
    pagebody = models.TextField()
    author = models.ForeignKey(
        'users.Store', # Наш пользователь из RegularUser
        on_delete = models.CASCADE,
    )
    #date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        """
        Хотим перенаправлять на ```DetailView``` данной страницы
        """
        return reverse("detail_page", args=[str(self.id)])
