from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'text',
            'status'
        ]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'status'
        ]
