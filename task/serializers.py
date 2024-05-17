from rest_framework import serializers
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source="user.fullname",read_only=True)
    title = serializers.CharField(required=True)
    due_date = serializers.DateTimeField(required=True)
    is_completed = serializers.BooleanField(read_only=True,default=False)

    class Meta:
        model = Task
        fields = "__all__"
