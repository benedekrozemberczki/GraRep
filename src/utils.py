import argparse
import numpy as np
import pandas as pd
import networkx as nx
from scipy import sparse
from texttable import Texttable


def create_inverse_degree_matrix(edges):
    graph = nx.from_edgelist(edges)
    ind = range(len(graph.nodes()))
    degs = [1.0/graph.degree(node) for node in range(graph.number_of_nodes())]
    D_1 = sparse.coo_matrix((degs,(ind,ind)),shape=(graph.number_of_nodes(), graph.number_of_nodes()),dtype=np.float32)
    return D_1

def normalize_adjacency(edges):
    """
    Method to calculate a sparse degree normalized adjacency matrix.
    :param graph: Sparse graph adjacency matrix.
    :return A: Normalized adjacency matrix.
    """
    D_1 = create_inverse_degree_matrix(edges)
    index_1 = [edge[0] for edge in edges] + [edge[1] for edge in edges]
    index_2 = [edge[1] for edge in edges] + [edge[0] for edge in edges]
    values = [1.0 for edge in edges] + [1.0 for edge in edges]
    A = sparse.coo_matrix((values,(index_1, index_2)),shape=D_1.shape,dtype=np.float32)
    A = A.dot(D_1)
    return A

def read_graph(edge_path):
    """
    Method to read graph and create a target matrix with pooled adjacency matrix powers up to the order.
    :param edge_path: Path to the ege list.
    :param order: Order of approximations.
    :return out_A: Target matrix.
    """
    print("Target matrix creation started.")
    edges = pd.read_csv(edge_path).values.tolist()
    A = normalize_adjacency(edges)
    return A

def tab_printer(args):
    """
    Function to print the logs in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    t = Texttable() 
    t.add_rows([["Parameter", "Value"]] +  [[k.replace("_"," ").capitalize(),v] for k,v in args.items()])
    print(t.draw())
