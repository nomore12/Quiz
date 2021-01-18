from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from django.urls import include, path, reverse

from quizzes.models import Quiz

# from quizzes.views import QuizViewSet


class QuizTestCase(TestCase):
    def setUp(self):
        Quiz.objects.create(title="첫 번째 퀴즈")
        Quiz.objects.create(title="두 번째 퀴즈")

    def test_create_model(self):
        first = Quiz.objects.get(title="첫 번째 퀴즈")
        second = Quiz.objects.get(title="두 번째 퀴즈")
        self.assertEqual(first.title, "첫 번째 퀴즈")
        self.assertEqual(second.title, "두 번째 퀴즈")


# class QuizHttpTestCase(APITestCase):
#     def test_quiz_api_get_index(self):
#         pk = 1
#         response = self.client.get(f"quiz/{pk}", format="json")
#         import pprint

#         pprint.pprint(dir(response))
#         pprint.pprint(response.request)
#         print(response.getvalue())
#         self.assertIn("test", response.content)


class QuizViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.quiz_data = {"pk": 1}
        self.response = self.client.get(reverse("quiz"), data={"pk": quiz_data}, format="json")

    def test_api_get_quiz(self):
        self.assertEqual(self.response.status_code, 200)
