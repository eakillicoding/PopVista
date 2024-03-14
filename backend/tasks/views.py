from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)
        return queryset


class LabelViewSet(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Label.objects.filter(owner=self.request.user)
        return queryset