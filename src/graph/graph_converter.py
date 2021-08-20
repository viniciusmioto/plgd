import networkx as nx
import os

current_path = os.path.dirname(__file__)
data_folder = os.path.join(current_path, 'data')

def convert_graph(file):
    degrees = []

    largest_degree = 0
    countdegree = 0
    smallest_degree = 1000000

    base_features_path = os.path.join(current_path, 'data/GRAPH_features_6.txt')
    base_features = open(base_features_path, "w")

    g = nx.read_gexf(os.path.join(data_folder, file))
    for i in g.nodes():
        if g.degree(i) > largest_degree:
            largest_degree = g.degree(i)
        if g.degree(i) < smallest_degree:
            smallest_degree = g.degree(i)
        countdegree += g.degree(i)

    mean = float(countdegree)/float(len(g.nodes()))

    count1, count2, count3 = 0, 0, 0
    for i in g.nodes():
        if g.degree(i) == largest_degree:
            count1 += 1
        if g.degree(i) == smallest_degree:
            count2 += 1


    density = nx.density(g)

    base_features.write("9"+" ")
    base_features.write(str(0)+":"+str(largest_degree)+" ")
    base_features.write(str(1)+":"+str(count1)+" ")
    base_features.write(str(2)+":"+str(smallest_degree)+" ")
    base_features.write(str(3)+":"+str(count2)+" ")
    base_features.write(str(4)+":"+str(mean)+" ")
    base_features.write(str(5)+":"+str(density)+" ")
    base_features.write("\n")

    del g
    del degrees
    base_features.close
