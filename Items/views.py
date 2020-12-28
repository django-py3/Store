from django.views.generic import ListView , DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy 
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class ItemsListView(ListView):
    model = Item
    template_name = "list_items.html"
    context_object_name = "list_items"

class ItemDetailView(DetailView):
    model = Item 
    template_name = "detail_item.html"
    context_object_name = "item"

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item 
    fields = ("title", "amount", "price")
    template_name = "update_item.html"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Получаем автора товара и сравниваем его с ТЕКУЩИМ ПОЛЬЗОВАТЕЛЕМ, который 
        выполняет запрос
        """ 
        article = self.get_object()
        if article.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "delete_item.html"
    success_url = reverse_lazy("items")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Получаем автора товара и сравниваем его с ТЕКУЩИМ ПОЛЬЗОВАТЕЛЕМ, который 
        выполняет запрос
        """ 
        article = self.get_object()
        if article.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "new_item.html"
    fields = ('title', 'price', 'amount')
    login_url = 'login'

    def form_valid(self, form):
        """
        Стандартный метод , который содержится в любом классе ....View
        Метод запускается при отправке любой формы
        """
        form.instance.owner = self.request.user 
        """
        У формы в поле автора = занести пользователя, который эту форму заполнял
        """
        return super().form_valid(form)