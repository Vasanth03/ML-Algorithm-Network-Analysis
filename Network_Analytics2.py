import pandas as pd
import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt

# Degree Centrality
G = pd.read_csv("/Users/vasanthdhanagopal/Desktop/360DigiTMG/2.DataScience-Sampath/12.Data Mining-Network Analysis/Network_Analytics_Datasets/Star.csv")

g = nx.Graph()

G1 = nx.read_edgelist(G,create_using = nx.Graph(), nodetype=int)

print(nx.info(g))

b = nx.degree_centrality(g)  # Degree Centrality
print(b) 

pos = nx.spring_layout(g, k = 0.15)
nx.draw_networkx(g, pos, node_size = 25, node_color = 'blue')

# closeness centrality
closeness = nx.closeness_centrality(g)
print(closeness)

## Betweeness Centrality 
b = nx.betweenness_centrality(g) # Betweeness_Centrality
print(b)

## Eigen-Vector Centrality
evg = nx.eigenvector_centrality(g) # Eigen vector centrality
print(evg)

# cluster coefficient
cluster_coeff = nx.clustering(g)
print(cluster_coeff)

# Average clustering
cc = nx.average_clustering(g) 
print(cc)
