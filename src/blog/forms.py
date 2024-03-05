from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            "content": forms.Textarea(attrs={
                'class': "form-control",
                "placeholder": "Message...",
                "cols": 45,
                "rows": 8
            })
        }
