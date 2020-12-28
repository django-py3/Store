from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pages 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.

class PageListView(ListView):
    model = Pages 
    template_name = "home.html"
    context_object_name = "pages"

class PageDetailView(DetailView):
    model = Pages 
    template_name = "detail_page.html"
    context_object_name = "page"

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Pages 
    template_name = "new_page.html"
    fields = ("title", "pagebody") #fields = '__all__' # какие поля мы будем заполнять в веб-форме
    login_url = 'login'
    def form_valid(self, form):
        """
        Стандартный метод , который содержится в любом классе ....View
        Метод запускается при отправке любой формы
        """
        form.instance.author = self.request.user 
        """
        У формы в поле автора = занести пользователя, который эту форму заполнял
        """
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Pages 
    template_name = "update_page.html"
    fields = ['title', 'pagebody'] # поля, которые я хочу обновлять
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Получаем автора СТАТЬИ и сравниваем его с ТЕКУЩИМ ПОЛЬЗОВАТЕЛЕМ, который 
        выполняет запрос
        """ 
        article = self.get_object()
        if article.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Pages 
    template_name = "delete_page.html"
    success_url = reverse_lazy("home")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Получаем автора СТАТЬИ и сравниваем его с ТЕКУЩИМ ПОЛЬЗОВАТЕЛЕМ, который 
        выполняет запрос
        """ 
        article = self.get_object()
        if article.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)