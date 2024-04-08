from django.contrib import admin
from .models import Category, Quiz, Question, Answer


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Quiz)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'users', 'description', 'created', 'category_quiz')
    prepopulated_fields = {
        'slug': ('title',)
    }


class AnswerModelAdmin(admin.TabularInline):
    model = Answer
    min_num = 4
    extra = 0
    list_display = ('title', 'is_correct')


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    inlines = [AnswerModelAdmin]

    class Meta:
        model = Question
