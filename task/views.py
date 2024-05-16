from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets, filters


class TaskViewSets(viewsets.ModelViewSet):
    http_method_names = ["get","patch", "post", "put", "delete"]
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('user').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user', 'is_completed', 'due_date']
    search_fields = ['title', 'description','user__firstname','user__lastname','user__email']
    ordering_fields = ['created_at']
   

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)  

    def paginate_results(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
