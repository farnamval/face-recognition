import shutil

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import os
from .Source import data_collector, trainer
from .constraits import constants as cnst, paths as pth
from .forms import UserRecognizerForm


# Create your views here.
from .models import UserRecognizer

recognizerNameTemp = ""


def register(request):
    #логика сохранения логина и пароля
    if request.method == 'POST':
        form = UserRecognizerForm(request.POST)
        if form.is_valid():
            recognizers = UserRecognizer.objects.all()
            for recognizer in recognizers:
                if str(recognizer.login) == str(form.cleaned_data['login']):
                    error = "This name is already exist. Try again"
                    form = UserRecognizerForm()
                    data = {
                        'form': form,
                        'error': error
                    }
                    return render(request, 'trainService/registrationPage.html', data)
            form.save()
            global recognizerNameTemp
            recognizerNameTemp = str(form.cleaned_data['login'])
            return redirect("/create-recognizer/upload-Data")
        else:
            error = "registration form is not valid"
            form = UserRecognizerForm()
            data = {
                'form': form,
                'error': error
            }
            return render(request, 'trainService/registrationPage.html', data)

    form = UserRecognizerForm()
    data = {
        'form': form
    }
    return render(request, 'trainService/registrationPage.html', data)


def uploadData(request):
    if request.method == 'POST':
        name = request.POST['name']
        images = request.FILES.getlist('images')
        name_dir = os.path.join(os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'People'), str(name))
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        for i in images:
            fs = FileSystemStorage()
            fs.save(i.name, i)
            shutil.move(os.path.join(pth.buffer_root, i.name), name_dir)
        for the_file in os.listdir(pth.buffer_root):
            file_path = os.path.join(pth.buffer_root, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    return render(request, 'trainService/uploadTrainData.html')

def train(request):

    people_path = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'People')
    faces_path = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'Faces')
    dtb_path = os.path.join(os.path.join(pth.users_data_root, recognizerNameTemp), 'cv2DataBases')
    if not os.path.exists(people_path):
        os.makedirs(people_path)
    if not os.path.exists(people_path):
        os.makedirs(faces_path)
    if not os.path.exists(dtb_path):
        os.makedirs(dtb_path)

    data_collector.collect_data(people_path, faces_path)
    trainer.train_recognizer(faces_path, dtb_path, cnst.face_width, cnst.face_height)
    #except BaseException:
        #return render(request, 'trainService/trainFailed.html')
    return render(request, 'trainService/trainSuccess.html')


def getUsers(request):
    if request.method == 'POST':
        return UserRecognizer.objects.all()


