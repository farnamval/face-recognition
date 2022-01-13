from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start),
    path('test-recognizer/', views.testRecognizer)
    #path('create-recognizer', include('trainService.views'), name='train')
]