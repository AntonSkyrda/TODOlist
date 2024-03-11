from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "tasks/index.html"


class CreateTaskView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class UpdateTaskView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagsListView(generic.ListView):
    model = Tag
    paginate_by = 5


class CreateTagView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class UpdateTagView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class DeleteTagView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


def mark_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = True
    task.save()
    return redirect('tasks:index')


def mark_task_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = False
    task.save()
    return redirect('tasks:index')
