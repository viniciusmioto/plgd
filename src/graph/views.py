from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . graphs import get_graph_features, classifier
from . forms import ModelsForm

def index(request):
    models_form = ModelsForm(request.POST or None)

    context = {
        'models_form': models_form
    }

    return render(request, 'index.html', context)

def predict_graph(request):
    
    # request data from the forms
    model_type = request.POST.get('model_type')
    graph_file = request.FILES['graph_file']
    
    # save data in data folder
    file_system = FileSystemStorage()
    file_path_name = file_system.save(graph_file.name, graph_file)
    file_path_name = file_system.url(file_path_name)

    # convert graph to a features vector
    graph_features = get_graph_features(graph_file.name)

    # prediction output
    prediction = classifier(graph_features, model_type)

    context = {
        'file_path_name':file_path_name, 
        'prediction': prediction,
        'model_type': model_type,
    }

    return render(request, 'index.html', context)

def models(request):
    context = {'a':1}
    return render(request, 'models.html', context)

def about(request):
    context = {'a':1}
    return render(request, 'about.html', context)