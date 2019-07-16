from django.contrib import admin
from .models import Page

admin.site.register(Page)  # Регистрируем данную модель в админ. панели Django
