from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from .models import Task
from rest_framework.decorators import action
from .serializers import TaskListSerializer,TaskCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets, filters


class TaskViewSets(viewsets.ModelViewSet):
    http_method_names = ["get","patch", "post", "put", "delete"]
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('user').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user', 'is_completed', 'due_date']
    search_fields = ['title', 'description','user__firstname','user__lastname','user__email']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)  

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return TaskListSerializer
        elif self.action in ["update","create","partial_update","delete"]:
           return TaskCreateSerializer
        else:
            return None

    def paginate_results(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['POST'],
        detail=True,
        permission_classes=[IsAuthenticated],
        serializer_class=None,
        url_path='set-completed',
    )
    def set_task_completed(self,request,pk=None):
        task = self.get_object()
        if task:
            task.is_completed = True
            task.save()
            return Response(
            {"success": True, "message": "Task set to completed successfully"},status=status.HTTP_200_OK
        )

        return Response(
            {"success": False, "error": "Task not found"},status=status.HTTP_404_NOT_FOUND
        )

    @action(
        methods=['POST'],
        detail=True,
        permission_classes=[IsAuthenticated],
        serializer_class=None,
        url_path='set-pending',
    )
    def set_task_pending(self, request, pk=None):
        task = self.get_object()
        if task:
            task.is_completed = False
            task.save()
            return Response(
                {"success": True, "message": "Task set to pending successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"success": False, "error": "Task not found"}, status=status.HTTP_404_NOT_FOUND
        )
