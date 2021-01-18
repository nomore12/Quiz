from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import include, path, reverse

from quizzes.models import Quiz
from quizzes.views import index


class QuizTestCase(TestCase):
    def setUp(self):
        Quiz.objects.create(title="첫 번째 퀴즈")
        Quiz.objects.create(title="두 번째 퀴즈")

    def test_create_model(self):
        first = Quiz.objects.get(title="첫 번째 퀴즈")
        second = Quiz.objects.get(title="두 번째 퀴즈")
        self.assertEqual(first.title, "첫 번째 퀴즈")
        self.assertEqual(second.title, "두 번째 퀴즈")


class QuizHttpTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_quiz_index(self):
        request = self.factory.get("/quiz")
        response = index(request)
        self.assertIn("hello", response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)