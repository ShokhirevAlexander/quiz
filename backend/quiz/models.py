from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='категория')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name='тест')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='описание')
    users = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True)
    category_quiz = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def get_absolute_url(self):
        return reverse('testing:category_slug', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name='вопрос')
    description = models.CharField(max_length=400, blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='question_image', verbose_name='изображение')
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, related_name='quiz_question')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100, verbose_name='ответ')
    is_correct = models.BooleanField(default=False, verbose_name='правильный ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return self.title

# class Result(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)