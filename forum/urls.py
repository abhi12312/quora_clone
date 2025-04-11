from django.urls import path
from .views import (
    QuestionListView, QuestionDetailView, QuestionCreateView, LikeAnswerView,
    RegisterView, LoginView, LogoutView, LoggedOutView
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('questions/ask/', QuestionCreateView.as_view(), name='question_create'),
    path('answers/<int:pk>/like/', LikeAnswerView.as_view(), name='like_answer'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logged-out/', LoggedOutView.as_view(), name='logged_out'),
]