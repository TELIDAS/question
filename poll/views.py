from rest_framework import generics
from .models import Question, UserAnswer, Answer
from . import serializers


class QuestionAPIView(generics.ListAPIView):
    serializer_class = serializers.QuestionSerializer
    queryset = Question.objects.all()


# class QuestionRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = serializers.QuestionSerializer
#     queryset = Question.objects.all()
#     lookup_field = ['id']


class UserAnswerAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.UserAnswersSerializers
    queryset = UserAnswer.objects.all()


class UserAnswerAll(generics.ListAPIView):
    serializer_class = serializers.UserAllSerializers
    queryset = UserAnswer.objects.all()
