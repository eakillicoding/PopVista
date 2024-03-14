from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task, Label


class TaskLabelModelTest(TestCase):
    def test_task_label_creation(self):
        user = User.objects.create_superuser(username='Test', password='pass123', email='test@admintest.com')
        label = Label.objects.create(name='Urgent', owner=user)
        task = Task.objects.create(title='Finish Backend Challenge', description='Soon', completion_status=False, owner=user)
        task.labels.add(label)
        task.save()
        self.assertEqual(task.owner, user)
        self.assertIn(label, task.labels.all())


class TaskLabelAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='Test', password='pass123', email='test@admintest.com')
        self.client.login(username='Test', password='pass123')
        
    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_labels(self):
        url = reverse('label-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)