from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response

from .serializers import (QuestionSerializer,
                          CategorySerializer,
                          AnswerSerializer,
                          QuestionAnswerSerializer)
from .models import Question, Answer, Category
from .services import process_answers


class QuestionApiView(views.APIView):
    def get(self, request, pk: int):
        result = []
        category = Category.objects.get(pk=pk)
        questions = category.question_set.all()
        for idx, question in enumerate(questions):
            q_serializer = QuestionSerializer(question)
            result.append(q_serializer.data)
            answers = question.answer_set.all()
            a_serializer = AnswerSerializer(answers, many=True)
            result[idx]['answers'] = []
            for answer in a_serializer.data:
                result[idx]['answers'].append(answer)

        return Response(result)

    def post(self, request):
        data = request.data
        correct_answers_count = process_answers(data)
        return Response(f'Вы ответили правильно на {correct_answers_count} вопросов')


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
