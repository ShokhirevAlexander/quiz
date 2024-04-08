from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from quiz.models import Category, Quiz, Question, Answer
from api.serializer import CategorySerializer, QuizSerializer


class CategoryList(viewsets.GenericViewSet):
    """ Категории тестов """
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizList(viewsets.GenericViewSet):
    """ Тесты """
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
