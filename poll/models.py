from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    title = models.CharField(max_length=255,
                             default="New Quiz",
                             verbose_name="Quiz Title")
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['id']

    TYPE = (
        (0, 'Multiple Choice'),
        (1, 'Single Choice'),
        (2, 'Text Question'),
    )

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name="Type of Question")
    title = models.CharField(max_length=255, verbose_name="Title")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date Created")
    is_active = models.BooleanField(
        default=False, verbose_name="Active Status")

    def __str__(self):
        return self.title


class Answer(models.Model):
    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['id']

    question = models.ForeignKey(Question,
                                 related_name='answer',
                                 on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255,
                                   verbose_name="Answer Text",
                                   blank=True)

    def __str__(self):
        return self.answer_text


class UserAnswer(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             related_name='user')
    question = models.ForeignKey(Question,
                                 on_delete=models.DO_NOTHING,
                                 related_name='user_question')
    answer = models.ManyToManyField(Answer,
                                    blank=True, )
    text = models.TextField(blank=True)

