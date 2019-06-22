from django.contrib import admin

from .models import Post, Tag, Category, Comment


admin.site.register(Post)  # Регистрируем данную модель в админ. панели Django

admin.site.register(Tag)

admin.site.register(Category)

admin.site.register(Comment)
