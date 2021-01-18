from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from quizzes.models import Quiz
from quizzes.serializers import QuizSerializer

# Create your views here.


# @api_view(
#     [
#         "GET",
#     ]
# )
# def index(request, pk):
#     print("request method: ", request.method)
#     if request.method == "GET":
#         print(request.data.get("pk", ""))
#         if pk == None:
#             return Response({"message": "bad request"})
#         quiz = Quiz.objects.get(pk=pk)
#         serializer = QuizSerializer(quiz)
#         return Response(serializer.data)
#     else:
#         return Response({"message": "bad request"})


@api_view(
    [
        "GET",
    ]
)
def index(request):
    return HttpResponse({"message": "hello"})


# class QuizAPIView(APIView):
#     def get(self, request, format=None):
#         title = Quiz.objects.get(request.data.get("title", ""))
#         serializer = Quiz(request.data)
#         return Response(serializer.data)


# class QuizViewSet(viewsets.ModelViewSet):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer