from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete
)


urlpatterns = [
    path("", TaskListView.as_view(), name="todo-list"),
    path("todo/create/", TaskCreateView.as_view(), name="todo-create"),
    path("todo/<int:pk>/update/", TaskUpdateView.as_view(), name="todo-update"),
    path("todo/<int:pk>/delete/", TaskDeleteView.as_view(), name="todo-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("todo/<int:pk>/complete/", complete, name="todo-complete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "app"
