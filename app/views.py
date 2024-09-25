from django.shortcuts import render
from django.views import generic
from .models import Task, Tag
from django.urls import reverse_lazy

from .forms import TagForm


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag

class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag-list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")