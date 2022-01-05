from django.shortcuts import render

# Create your views here.

def gui(request):
    return render(request, 'main/gui.html')

def uploadTrain(request):
    return render(request, 'main/uploadTrain.html')

def train(request):
    return render(request, 'main/train.html')

def uploadSource(request):
    return render(request, 'main/uploadSource.html')

def recognize(request):
    return render(request, 'main/recognize.html')
