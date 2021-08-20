from rest_framework import serializers
from .models import Quizzes, Question, Answer, UserAnswer
from django.contrib.auth.models import User


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'question'
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'title', 'answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'quiz',
            'title',
            'answer',
        ]


class UserAnswersSerializers(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=Question.objects.all())

    user = serializers.PrimaryKeyRelatedField(write_only=True,
                                              queryset=User.objects.all())

    class Meta:
        model = UserAnswer
        fields = [
            'question',
            'question_id',
            'user',
            'answer',
            'text',
        ]


class UserAllSerializers(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ('question',
                  'user',
                  'answer',
                  'text')
