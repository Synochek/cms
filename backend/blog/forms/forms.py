from django import forms

from ..models import Comment, Feedback


class CommentForm(forms.ModelForm):
    '''Форма комментария'''
    class Meta:
        model = Comment
        fields = ('text',)  # все поля - __all__
        # exclude = .. позволяет исключать ненужные поля


class FeedbackForm(forms.ModelForm):
    '''Форма обратной связи'''
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ('created',)
