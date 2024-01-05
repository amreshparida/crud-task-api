from django.urls import path
from rest_framework.throttling import UserRateThrottle
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView


#below are our api routes for tasks management
urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(throttle_classes=[UserRateThrottle]), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(throttle_classes=[UserRateThrottle]), name='task-retrieve-update-destroy'),
]
