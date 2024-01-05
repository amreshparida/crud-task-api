from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Testing the task API', 'completed': False}
        self.task = Task.objects.create(**self.task_data)
        self.url = f'/api/v1/tasks/{self.task.id}/'

    # get all tasks test
    def test_get_all_tasks(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #create tasks test
    def test_create_task(self):
        response = self.client.post('/api/v1/tasks/', data=self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #get single task test
    def test_get_single_task(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #update single test
    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'Updated description', 'completed': True}
        response = self.client.put(self.url, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #delete task test
    def test_delete_task(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
