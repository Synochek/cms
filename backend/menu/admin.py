from django.contrib import admin
from .models import Menu, ItemsMenu
from mptt.admin import MPTTModelAdmin


admin.site.register(Menu)  # Регистрируем данную модель в админ. панели Django
admin.site.register(ItemsMenu)
