from .models import Store

# Заготовки интерфейса пользовательской модели
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class StoreUserCreationForm(UserCreationForm):
    """
    Наш интерфейс взаимодействия с нашей Store моделью
    Создание юзера
    """
    class Meta(UserCreationForm.Meta):
        model = Store
        fields = UserCreationForm.Meta.fields + ('inn','year_open',) 
        # При создании пользователя еще хотим указывать инн и год открытия

class StoreUserChangeForm(UserChangeForm):
    """
    Наш интерфейс взаимодействия с нашей Store моделью
    Редактирование юзера
    """
    class Meta(UserChangeForm.Meta):
        model = Store
        fields = UserChangeForm.Meta.fields 