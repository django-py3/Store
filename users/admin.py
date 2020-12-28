from django.contrib import admin
from .models import Store
from .forms import StoreUserChangeForm, StoreUserCreationForm


# Низкоуровневый админский интерфейс
from django.contrib.auth.admin import UserAdmin 
# Register your models here.


# Создаем свой интерфейс по взаимодействию с моделью на основе UserAdmin
class StoreUserAdmin(UserAdmin):
    add_form = StoreUserCreationForm
    form = StoreUserChangeForm
    model = Store
    list_display = ["username", "email", "inn", "year_open"]


# Регистрируем интерфейс в панель
admin.site.register(Store, StoreUserAdmin)
