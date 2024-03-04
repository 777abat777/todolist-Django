from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='todos', on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    todo = models.ForeignKey(
        'Todo', related_name='tasks', on_delete=models.CASCADE)
