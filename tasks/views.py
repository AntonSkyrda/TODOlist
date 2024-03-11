from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "tasks/index.html"


class TagsListView(generic.ListView):
    model = Tag
    paginate_by = 10

