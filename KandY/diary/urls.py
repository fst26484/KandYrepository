from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('white', views.white, name='white'),
    path('view', views.view, name='view'),
    path('question', views.question, name='question'),
]