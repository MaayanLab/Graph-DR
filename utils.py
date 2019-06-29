'''Util functions for DR
'''
from collections import Counter, OrderedDict

import numpy as np
import networkx as nx
import igraph as ig
from sklearn import preprocessing, neighbors
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from sklearn.metrics.pairwise import pairwise_distances

import seaborn as sns
# pretty colors
COLORS10 = sns.color_palette("tab10", 10).as_hex()
sns.set_palette(COLORS10)

try:
    from cyrest_helpers import *
except ModuleNotFoundError:
    pass

def min_max_scale(X_train, X_test):
    '''Scale data to (0, 1)'''
    preprocessor = preprocessing.MinMaxScaler().fit(X_train)
    X_train = preprocessor.transform(X_train)
    X_test = preprocessor.transform(X_test)
    return X_train, X_test

def get_random_block_from_data(data, batch_size):
    start_index = np.random.randint(0, len(data) - batch_size)
    return data[start_index:(start_index + batch_size)]


def plot_embed(X_coords, labels, figsize=(6, 6)):
    '''Scatter plot for the coordinates colored by their labels'''
    X_coords = preprocessing.MinMaxScaler(feature_range=(-1, 1)).fit_transform(X_coords[:, :2])

    fig, ax = plt.subplots(figsize=figsize)
    scatter_proxies = []
    colors = [COLORS10[l] for l in labels]
    ax.scatter(X_coords[:, 0], X_coords[:, 1], s=5, c=colors, edgecolor='none')
    for i in range(10):
        scatter_proxy = Line2D([0],[0], ls="none", 
                               c=COLORS10[i], 
                               marker='o', 
                               markersize=5, 
                               markeredgecolor='none')    
        scatter_proxies.append(scatter_proxy)
    
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(scatter_proxies, map(str, range(10)), 
              numpoints=1,
              loc='center left', bbox_to_anchor=(1, 0.5))

    fig.tight_layout()
    return ax

  
def compute_adjcency_mat(X, metric='euclidean'):
    pdist = pairwise_distances(X, metric=metric)
    adj_mat = 1 - pdist / pdist.max()
    # remove 1's on the diagnal
    adj_mat -= np.eye(X.shape[0])
    return adj_mat


def plot_degree_distribution(G):
    """G: a nx.Graph object
    """
    fig, ax = plt.subplots(figsize=(5,5))
    
    degrees = [k for n, k in G.degree()]
    degrees = dict(Counter(degrees))
    x = degrees.keys()
    y = degrees.values()

    ax.scatter(x, y, s=10, alpha=.6)
    ax.set_xlabel('Degree', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)    
    ax.set_xscale('log')
    ax.set_yscale('log')
    fig.tight_layout()
    return ax
    

def create_knn_graph(X, k=30, metric='euclidean'):
    '''Create a graph from a data matrix (sample x features).
    '''
    adj_mat = neighbors.kneighbors_graph(X, k, mode='connectivity', metric=metric)
    G = nx.from_scipy_sparse_matrix(adj_mat)
    return G

# thresholding-Firework
def create_graph_by_threshold(adj_mat, percentile):
    triu_idx = np.tril_indices(adj_mat.shape[0], 1)
    thresold = np.percentile(adj_mat[triu_idx], percentile)
    adj_mat_ = adj_mat.copy()
    adj_mat_[adj_mat<thresold] = 0
    G = nx.from_numpy_matrix(adj_mat_)
    return G

def create_graph_by_threshold_knn(adj_mat, percentile, k=1, X=None):
    '''combine the graph from `create_graph_by_threshold` with a kNN graph.
    '''
    G_thres = create_graph_by_threshold(adj_mat, percentile)
    G_knn = create_knn_graph(X, k=k)
    return nx.compose(G_thres, G_knn)


def nx_graph_to_igraph(G):
    '''convert nx.Graph to ig.Graph via adjacency matrix
    '''
    g = ig.Graph.Adjacency((nx.to_numpy_matrix(G) > 0).tolist(), mode=ig.ADJ_UNDIRECTED)
    return g


def network_layout(G, layout='drl', **layout_kwargs):
    '''First convert to ig.Graph object, then apply layout functions.
    layout can be: ['drl', 'fr', 'kk', 'lgl', ...]
    See: https://igraph.org/python/doc/tutorial/tutorial.html#layout-algorithms
    '''
    g = nx_graph_to_igraph(G)
    # Perform Fruchterman-Reingold force-dirceted layout algorithm for the graph
    layt = g.layout(layout, **layout_kwargs)
    coords = np.array(layt.coords)
    return coords

def plot_network(layout):
    return
