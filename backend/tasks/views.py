from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated, IsOwner]