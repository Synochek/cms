from django.contrib import admin
from .models import Menu, ItemsMenu

admin.site.register(Menu)  # Регистрируем данную модель в админ. панели Django
admin.site.register(ItemsMenu)
