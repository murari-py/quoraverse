from django.urls import path

from .views import (
    QuestionListCreateView,
    QuestionDetailView,
    post_answer,like_answer
)

urlpatterns = [
    path('', QuestionListCreateView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('questions/<int:pk>/answer/', post_answer, name='post_answer'),
    path('answer/<int:pk>/like/', like_answer, name='like_answer'),

]
