from django import forms
from .models import Tag, Task

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"