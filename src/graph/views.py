from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . graphs import convert_graph, classifier

def index(request):
    context = {'a':1}
    return render(request, 'index.html', context)

def predict_graph(request):
    
    # save graph file in data folder
    file_object = request.FILES['file_path']
    file_system = FileSystemStorage()
    file_path_name = file_system.save(file_object.name, file_object)
    file_path_name = file_system.url(file_path_name)

    # convert graph to a features vector
    convert_graph(file_object.name)

    # prediction output
    prediction = classifier()
    if prediction[0] < 1:
        prediction_text = 'NOT Power-Law'
    else:
        prediction_text = 'Power-Law'

    context = {'file_path_name':file_path_name, 'prediction': prediction_text}

    return render(request, 'index.html', context)

def models(request):
    context = {'a':1}
    return render(request, 'models.html', context)