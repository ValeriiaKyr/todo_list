from django import forms
from .models import Tag, Task

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateInput(attrs={
            "type": "datetime-local",
        }))
    class Meta:
        model = Task
        fields = "__all__"
