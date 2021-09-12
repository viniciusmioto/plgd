from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . graphs import get_graph_features, classifier

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
    graph_features = get_graph_features(file_object.name)

    # prediction output
    prediction = classifier(graph_features)
    prediction_text = 'Power-Law' if prediction[0] == 1 else 'NOT Power-Law'

    context = {'file_path_name':file_path_name, 'prediction': prediction_text}

    return render(request, 'index.html', context)

def models(request):
    context = {'a':1}
    return render(request, 'models.html', context)

def about(request):
    context = {'a':1}
    return render(request, 'about.html', context)