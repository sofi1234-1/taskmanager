from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .serializers import TaskSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_GET
@require_GET
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Task Management API",
        "available_endpoints": [
            "/api/tasks/",
            "/api/users/",
            "/api/auth/token/",
            "/api/auth/token/refresh/"
        ]
    })

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        task = self.get_object()
        if task.status == 'Completed':
            raise serializers.ValidationError("Cannot edit a completed task.")
        serializer.save()
