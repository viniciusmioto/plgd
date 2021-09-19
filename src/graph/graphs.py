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
def classifier(graph_features):

    model_path = os.path.join(current_path, '../models/knn_model.pkl')
    model = pickle.load(open(model_path,'rb'))

    prediction = model.predict(graph_features)

    return prediction
