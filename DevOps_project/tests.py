# userapp/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import User
from .utils import VisitCounter

class UserListViewTest(TestCase):
    def test_user_list_view(self):
        User.objects.create(username='user1', email='user1@example.com', first_name='John', last_name='Doe')
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'user1')
        self.assertContains(response, 'user1@example.com')
        self.assertContains(response, 'John')
        self.assertContains(response, 'Doe')

class VisitCountViewTest(TestCase):
    def test_visit_count_view(self):
        response = self.client.get(reverse('visit-count'))
        self.assertEqual(response.status_code, 200)
        counter = VisitCounter()
        count = counter.get_count()
        self.assertEqual(int(response.json()['visit_count']), count + 1)
