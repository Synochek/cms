from django import forms

from cms.blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')  # все поля - __all__
            #  exclude = .. позволяет исключать ненужные поля
