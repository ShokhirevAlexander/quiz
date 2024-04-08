from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.views import CategoryList, QuizList


routers = SimpleRouter()
routers.register('category', CategoryList)
routers.register('quiz', QuizList,)

urlpatterns = [
    path('', include(routers.urls)),
]
