from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . graphs import convert_graph, classifier

def index(request):
    context = {'a':1}
    return render(request, 'index.html', context)

def predict_graph(request):
    file_object = request.FILES['file_path']
    file_system = FileSystemStorage()
    file_path_name = file_system.save(file_object.name, file_object)
    file_path_name = file_system.url(file_path_name)
    context = {'file_path_name':file_path_name}
    convert_graph(file_object.name)
    print(classifier(file_object.name))

    return render(request, 'index.html', context)