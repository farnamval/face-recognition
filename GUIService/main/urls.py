from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.gui),
    path('upload-train/', views.uploadTrain),
    path('train/', views.train),
    path('upload-source/', views.uploadSource),
    path('recognize/', views.recognize)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)