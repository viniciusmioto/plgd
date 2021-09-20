import pickle, os
import networkx as nx
import numpy as np
import statistics as sts

current_path = os.path.dirname(__file__)
data_folder = os.path.join(current_path, '../data')

# convert graph to a features vector with six features
def get_graph_features(file):

    graph = nx.read_gexf(os.path.join(data_folder, file))

    max_degree = max(dict(nx.degree(graph)).values())
    min_degree = min(dict(nx.degree(graph)).values())
    avg_degree = sts.mean(dict(nx.degree(graph)).values())
    qtd_max_degree = list(dict(nx.degree(graph)).values()).count(max_degree)
    qtd_min_degree = list(dict(nx.degree(graph)).values()).count(min_degree)
    density = nx.density(graph)
    
    return np.array([max_degree, qtd_max_degree, min_degree, qtd_min_degree, avg_degree, density]).reshape(1, -1)


# predict graph classification with a ML model
def classifier(graph_features, model_type):

    if model_type == '#1':
        model_path = os.path.join(current_path, '../models/knn_model.pkl')
    elif model_type == '#2':
        model_path = os.path.join(current_path, '../models/svm_model.pkl')
    elif model_type == '#3':
        model_path = os.path.join(current_path, '../models/forest_model.pkl')
    elif model_type == '#4':
        model_path = os.path.join(current_path, '../models/grad_boost_model.pkl')
    else:
        print('No model_type specified!')

    model = pickle.load(open(model_path,'rb'))
    prediction = model.predict(graph_features)

    return prediction
