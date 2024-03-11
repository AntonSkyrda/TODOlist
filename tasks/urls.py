from django.contrib import admin
from django.urls import path, include

from .views import TaskListView, TagsListView


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/",TagsListView.as_view(), name="tag-list")
]

app_name = "tasks"
