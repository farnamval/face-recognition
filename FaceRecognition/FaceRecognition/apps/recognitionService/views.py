import os
import shutil

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from glob import glob

# Create your views here.
from .source import recognizer
from .constraits import paths as pth, constants as cnst
from trainService.models import UserRecognizer
from trainService.forms import UserRecognizerForm

# Create your views here.

recognizerNameTemp = ""

def start(request):
    return render(request, "recognitionService/startPage.html")

def testRecognizer(request):
    recognizer.recognize_people(pth.cv2DataBases_path_test, cnst.fisher_database, cnst.lbph_database,
                                pth.source_path_test, cnst.face_width, cnst.face_height)
    return render(request, "recognitionService/recognize-complete.html")

def loginRecognizer(request):
    if request.method == 'POST':
        form = UserRecognizerForm(request.POST)
        if form.is_valid():
            recognizers = UserRecognizer.objects.all()
            for recognizer in recognizers:
                if str(recognizer.login) == str(form.cleaned_data['login']) and \
                        str(recognizer.password) == str(form.cleaned_data['password']):
                    global recognizerNameTemp
                    recognizerNameTemp = str(form.cleaned_data['login'])
                    return redirect("/recognize/upload-source/")
            error = "Incorrect login or password. Try again"
            form = UserRecognizerForm()
            data = {
                'form': form,
                'error': error
            }
            return render(request, 'recognitionService/loginPage.html', data)
        else:
            error = "log in form is not valid"
            form = UserRecognizerForm()
            data = {
                'form': form,
                'error': error
            }
            return render(request, 'recognitionService/loginPage.html', data)

    form = UserRecognizerForm()
    data = {
        'form': form
    }
    return render(request, 'recognitionService/loginPage.html', data)

def uploadSource(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        name_dir = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'Source')
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        for i in images:
            fs = FileSystemStorage()
            fs.save(i.name, i)
            shutil.move(os.path.join(pth.buffer_root, i.name), name_dir)
    return render(request, 'recognitionService/uploadSource.html')


def launchRecognizer(request):
    dtb_path = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'cv2DataBases')
    src_path = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'Source')

    fcs_path = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'Faces')
    peoples = os.listdir(fcs_path)
    names = ['', ]
    names.extend(peoples)


    recognizer.recognize_people(dtb_path, cnst.fisher_database, cnst.lbph_database,
                                src_path, cnst.face_width, cnst.face_height, names)
    for the_file in os.listdir(src_path):
        file_path = os.path.join(src_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    return render(request, "recognitionService/recognize-complete.html")

