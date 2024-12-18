# quiz/urls.py
from django.urls import path
from quiz.views import get_random_quiz,get_attempted_questions,submit_answer

urlpatterns = [
    path('question/', get_random_quiz, name='get_random_quiz'),
    path('submit/', submit_answer , name='submit_answer'),
    path('results/', get_attempted_questions , name='submit_answer'),
]