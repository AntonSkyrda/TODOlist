from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return f"{self.title}, {self.done}, {self.date}, {self.tags}, {self.description}"
