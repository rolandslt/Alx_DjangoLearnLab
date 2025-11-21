from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 255}),
            'content': forms.Textarea(attrs={'maxlength': 5000}),
        }
