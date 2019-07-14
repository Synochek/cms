from django import forms

from ..models import Comment


class CommentForm(forms.ModelForm):
    '''Форма комментария'''
    class Meta:
        model = Comment
        fields = ('text',)  # все поля - __all__
        # exclude = .. позволяет исключать ненужные поля
