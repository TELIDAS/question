from django.urls import path
from . import views
urlpatterns = [
    path('question/', views.QuestionAPIView.as_view(), name='questions'),
    # path('question/<int:id>/', views.QuestionRetrieveAPIView.as_view(), name='questions-retrieve'),
    path('question/answers/', views.UserAnswerAPIView.as_view(), name='user-answers'),
    path('answers-all/', views.UserAnswerAll.as_view(), name='all-done-answers'),
]