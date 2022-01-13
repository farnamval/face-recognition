
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from . import views
from django.shortcuts import render
from .source import recognizer
from .constraits import paths, constants as cnst

# Create your views here.
def start(request):
    return render(request, "recognitionService/startPage.html")

def testRecognizer(request):
    recognizer.recognize_people(paths.cv2DataBases_path_test, cnst.fisher_database, cnst.lbph_database,
                                paths.source_path_test, cnst.face_width, cnst.face_height)
    return render(request, "recognitionService/recognize-complete.html")
