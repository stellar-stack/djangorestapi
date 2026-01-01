from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer

class TaskLiStCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset =Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAdminUser]