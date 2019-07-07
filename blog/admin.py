from django.contrib import admin

from .models import Post, Tag, Category, Comment, Feedback

from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin, admin.ModelAdmin):  # Вложенность категорий с отступами
    mptt_level_indent = 20
    list_display = ('name', 'active')
    list_editable = ('active',)
    list_filter = ('parent',)
    search_fields = ('title',)

    prepopulated_fields = {'slug': ('name',)}


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1  # добавляет поле после комметария


class PostAdmin(admin.ModelAdmin):  # Статья
    list_display = ('id', 'title', 'created', 'active', 'sort', 'view', 'category')  # отображение полей быстрого
    # редактирования
    list_display_links = ('title',)  # Кликабельные поля-ссылки
    list_filter = ('category', 'created')  # фильтр справа
    list_editable = ('sort', 'active')  # редактируемые элементы в таблице
    search_fields = ('title',)  # поле поиска
    inlines = [CommentInline]  # Встроенные комментарии
    readonly_fields = ('view',)
    # fields = ('category', 'title', 'sub_title', 'text', 'active', 'sort')
    filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': ('sort', 'title', 'sub_title', 'mini_text', 'text', 'active')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('category', 'tags', 'slug'),
        }),
        ('Additional info', {
            'classes': ('collapse',),
            'fields': ('view', 'publish_date'),
        }),
    )
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):  # Параметры админки для тегов
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)

    prepopulated_fields = {'slug': ('name',)}


class TagComment(admin.ModelAdmin):  # Параметры админки для комментариев
    list_display = ('id', 'user', 'post', 'moderation', 'created')
    list_display_links = ('post',)
    list_editable = ('moderation',)
    list_filter = ('text',)
    search_fields = ('name',)


class FeedbackAdmin(admin.ModelAdmin):  # Параметры админки для формы фидбек
    list_display = ('name', 'email', 'created')
    list_filter = ('email',)
    search_fields = ('text',)


admin.site.register(Post, PostAdmin)  # Регистрируем данную модель в админ. панели Django
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, TagComment)
admin.site.register(Feedback, FeedbackAdmin)