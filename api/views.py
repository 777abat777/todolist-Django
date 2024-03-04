from rest_framework import generics
from rest_framework import viewsets
from . import serializers
from django.contrib.auth.models import User
from .models import Todo, Task
from django.shortcuts import get_object_or_404


class TodoList(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer

    def get_queryset(self):
        return Todo.objects.all()


class TaskList(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
