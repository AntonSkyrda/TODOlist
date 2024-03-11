from django.urls import path

from .views import (
    TaskListView,
    TagsListView,
    CreateTaskView,
    CreateTagView,
    UpdateTaskView,
    DeleteTaskView,
    UpdateTagView,
    DeleteTagView,
    mark_task_undone,
    mark_task_done,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("task/create/", CreateTaskView.as_view(), name="task-create"),
    path("tag/create/", CreateTagView.as_view(), name="tag-create"),
    path("task/<int:pk>/update/", UpdateTaskView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", DeleteTaskView.as_view(), name="task-delete"),
    path("tag/<int:pk>/update/", UpdateTagView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", DeleteTagView.as_view(), name="tag-delete"),
    path('task/<int:pk>/mark_done/', mark_task_done, name='mark-task-done'),
    path('task/<int:pk>/mark_undone/', mark_task_undone, name='mark-task-undone'),

]

app_name = "tasks"
