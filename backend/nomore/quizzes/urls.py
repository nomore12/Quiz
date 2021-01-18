from django.urls import path
from quizzes import views
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register("quiz", QuizViewSet, basename="quiz")
# urlpatterns = router.urls


urlpatterns = [path("", views.index, name="index")]
