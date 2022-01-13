from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register),
    path('check-login/', views.checkLogin),
    path('upload-Data/', views.uploadData),
    path('train/', views.train)
    #path('create-recognizer', include('trainService.views'), name='train')
]