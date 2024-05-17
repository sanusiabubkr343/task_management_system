from rest_framework import serializers
from .models import Task
class TaskListSerializer(serializers.ModelSerializer):
    user_fullname = serializers.StringRelatedField(source="user.fullname",read_only=True)
    class Meta:
        model = Task
        fields = "__all__"

class TaskCreateSerializer(serializers.ModelSerializer):

        title = serializers.CharField(required=True)
        due_date = serializers.DateTimeField(required=True)

        class Meta:
           model = Task
           fields = ["id","user","title", "description", "due_date",]
           read_only_fields = ["id","user"]
           
