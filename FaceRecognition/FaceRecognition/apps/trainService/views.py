import shutil

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import os
from .Source import data_collector, trainer
from .constraits import constants as cnst, paths as pth


# Create your views here.
def register(request):
    #логика сохранения логина и пароля
    return render(request, 'trainService/registrationPage.html')

def checkLogin(request):
    #проврека на сущесвтование введенного логина
    if(1 > 0):
        return redirect("/create-recognizer/upload-Data")
    else:
        return render(request, 'trainService/registrationFailed.html')

def uploadData(request):
    if request.method == 'POST':
        name = request.POST['name']
        images = request.FILES.getlist('images')
        name_dir = os.path.join(os.path.join(pth.test_data_root, 'People'), str(name))
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        for i in images:
            fs = FileSystemStorage()
            fs.save(i.name, i)
            shutil.move(os.path.join(pth.buffer_root, i.name), name_dir)
    return render(request, 'trainService/uploadTrainData.html')

def train(request):
    #try:
    data_collector.collect_data(pth.people_path_test, pth.faces_path_test)
    trainer.train_recognizer(pth.faces_path_test, pth.cv2DataBases_path_test, cnst.face_width, cnst.face_height)
    #except BaseException:
        #return render(request, 'trainService/trainFailed.html')
    return render(request, 'trainService/trainSuccess.html')



