from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'isDone', 'todo']


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'owner', 'tasks']
