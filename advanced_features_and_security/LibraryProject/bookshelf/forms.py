from django import forms
from .models import Article

from django import forms
from .models import Article  # or any model you want the form for

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Article  # replace with your model if different
        fields = ['title', 'content']  # include the fields you want in the f