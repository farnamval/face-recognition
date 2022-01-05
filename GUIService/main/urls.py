from django.urls import path
from . import views

urlpatterns = [
    path('', views.gui),
    path('upload-train/', views.uploadTrain),
    path('train/', views.train),
    path('upload-source/', views.uploadSource),
    path('recognize/', views.recognize)
]
