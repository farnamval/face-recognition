from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start),
    path('test-recognizer/', views.testRecognizer),
    path('log-in-user-recognizer/', views.loginRecognizer),
    path('upload-source/', views.uploadSource),
    path('launch-recognizer/', views.launchRecognizer)

    #path('create-recognizer', include('trainService.views'), name='train')
]