from django import forms

from ..models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)  # все поля - __all__
            #  exclude = .. позволяет исключать ненужные поля

# class feedbackForm(forms.ModelForm):
#     class Meta:
#         model =