from django.urls import path

from .views import QuestionApiView, CategoryApiView

urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('questions/', QuestionApiView.as_view()),
    path('questions/<int:pk>/', QuestionApiView.as_view()),
]
