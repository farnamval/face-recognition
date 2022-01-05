import os
import shutil
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .Origin.trainer import train_recognizer
from .Origin.data_collector import collect_data
from .Origin import image_resizing
from GUIService.settings import MEDIA_ROOT


people_path = os.path.join(MEDIA_ROOT, 'People')
faces_path = os.path.join(MEDIA_ROOT, 'Faces')
databases_path = os.path.join(MEDIA_ROOT, 'Databases')
source_path = os.path.join(MEDIA_ROOT, 'Source')
lbph_database = 'LBPH_database.yml'
fisher_database = 'Fischer_database.yml'
face_width = 500
face_height = 500

def gui(request):
    return render(request, 'main/gui.html')

def uploadTrain(request):
    if request.method == 'POST':
        name = request.POST['name']
        images = request.FILES.getlist('images')

        name_dir = os.path.join(os.path.join(MEDIA_ROOT, 'People'), str(name))
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        for i in images:
            fs = FileSystemStorage()
            fs.save(i.name, i)
            shutil.move(os.path.join(MEDIA_ROOT, i.name), name_dir)
    return render(request, 'main/uploadTrain.html')

def train(request):
    collect_data(people_path, faces_path)
    train_recognizer(faces_path, databases_path, face_width, face_height)
    return render(request, 'main/gui.html')

def uploadSource(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        name_dir = os.path.join(MEDIA_ROOT, 'Source')
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        for i in images:
            fs = FileSystemStorage()
            fs.save(i.name, i)
            shutil.move(os.path.join(MEDIA_ROOT, i.name), name_dir)
    return render(request, 'main/uploadSource.html')

def recognize(request):
    return render(request, 'main/recognize.html')
