"""Running GraRep"""

from grarep import GraRep
from param_parser import parameter_parser
from utils import read_graph, tab_printer

def learn_model(args):
    """
    Method to create adjacency matrix powers, read features, and learn embedding.
    :param args: Arguments object.
    """
    A = read_graph(args.edge_path)
    model = GraRep(A, args)
    model.optimize()
    model.save_embedding()

if __name__ == "__main__":
    args = parameter_parser()
    tab_printer(args)
    learn_model(args)
