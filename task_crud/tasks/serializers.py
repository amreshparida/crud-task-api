from rest_framework import serializers
from .models import Task

# model task serializer 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']
