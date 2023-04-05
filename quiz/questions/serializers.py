from rest_framework import serializers

from .models import Question, Answer, Category


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionAnswerSerializer(serializers.Serializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
