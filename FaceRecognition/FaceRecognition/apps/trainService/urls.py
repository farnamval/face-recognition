from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register),
    path('upload-Data/', views.uploadData),
    path('train/', views.train),
    path('get-users-database/', views.getUsers)
    #path('create-recognizer', include('trainService.views'), name='train')
]