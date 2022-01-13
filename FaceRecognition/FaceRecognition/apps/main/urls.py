from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('recognize/', include('recognitionService.urls'), name='recognize'),
    path('create-recognizer/', include('trainService.urls'), name='train')
]