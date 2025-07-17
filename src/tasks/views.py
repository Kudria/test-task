from rest_framework import viewsets
from rest_framework import mixins

from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskUpdateSerializer


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Task.objects.all()
    filterset_fields = ('status',)
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action == 'update':
            return TaskUpdateSerializer
        else:
            return TaskSerializer
