from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):  # Параметры админки для формы фидбек
    list_display = ('name', 'email', 'created')
    list_filter = ('email',)
    search_fields = ('text',)
    readonly_fields = ('name', 'email', 'created', 'text', 'phone')


admin.site.register(Feedback, FeedbackAdmin)