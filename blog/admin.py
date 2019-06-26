from django.contrib import admin

from .models import Post, Tag, Category, Comment

from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):  # Вложенность категорий с отступами
    mptt_level_indent = 20


admin.site.register(Post)  # Регистрируем данную модель в админ. панели Django
admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
