# myapp/tests.py
from django.test import TestCase, RequestFactory
from django.http import JsonResponse
from unittest.mock import patch

# from DevOps_project.utils import VisitCounter
from .views import get_people


class TestGetPeopleView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("DevOps_project.views.Person.objects.all")
    def test_get_people_view(self, mock_person_objects):
        # Create a mock Person instance for testing
        mock_person = MockPerson(
            username="testuser",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )

        mock_person_objects.return_value = [mock_person]

        # Create a request to the view
        request = self.factory.get("/people/")
        response = get_people(request)

        # Verify the response
        expected_response = JsonResponse(
            [
                {
                    "username": mock_person.username,
                    "email": mock_person.email,
                    "first_name": mock_person.first_name,
                    "last_name": mock_person.last_name,
                }
            ],
            safe=False,
        )

        self.assertEqual(response.content, expected_response.content)
        self.assertEqual(response.status_code, expected_response.status_code)


class MockPerson:
    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


# class TestGetVisitCountView(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     @patch('DevOps_project.utils.VisitCounter')
#     def test_get_visit_count_view(self, mock_visit_counter):
#         # Create a mock VisitCounter instance
#         mock_counter = Mock(VisitCounter)

#         # Configure the mock VisitCounter class to return the mock instance
#         mock_visit_counter.return_value = mock_counter

#         # Mock the increment method of the counter
#         mock_counter.increment.side_effect = None

#         # Mock the get_count method of the counter to return 42
#         mock_counter.get_count.return_value = 42

#         # Create a request to the view
#         request = self.factory.get('/visit-count/')
#         response = get_visit_count(request)

#         # Verify the response
#         expected_response = JsonResponse({"visit_count": 42})

#         self.assertEqual(response.content, expected_response.content)
#         self.assertEqual(response.status_code, expected_response.status_code)
