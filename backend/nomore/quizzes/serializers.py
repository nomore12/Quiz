from quizzes.models import Quiz
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "title", "created_at"]

    # title = serializers.CharField(max_length=100)