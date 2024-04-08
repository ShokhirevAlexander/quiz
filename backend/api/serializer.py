from rest_framework import serializers, fields
from quiz.models import Category, Quiz, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug', 'description')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('title', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer()

    class Meta:
        model = Question
        fields = ('title', 'description', 'image', 'quiz', 'answer')


class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Quiz
        fields = ('title', 'slug', 'description', 'users', 'created', 'category_quiz', 'question')
