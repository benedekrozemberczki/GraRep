"""Parsing parameters from the command line."""

import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it gives an embedding of Cora.
    The default hyperparameters give a good quality representation without grid search.
    Representations are sorted by node ID.
    """
    parser = argparse.ArgumentParser(description="Run GraRep.")


    parser.add_argument('--edge-path',
                        nargs='?',
                        default='./input/edges/cora.csv',
	                help='Input edges.')

    parser.add_argument('--output-path',
                        nargs='?',
                        default='./output/cora_grarep.csv',
	                help='Output embedding.')

    parser.add_argument('--dimensions',
                        type=int,
                        default=16,
	                help='Number of dimensions. Default is 16.')

    parser.add_argument('--order',
                        type=int,
                        default=5,
	                help='Approximation order. Default is 5.')

    parser.add_argument('--seed',
                        type=int,
                        default=42,
	                help='Random seed. Default is 42.')

    parser.add_argument('--iterations',
                        type=int,
                        default=20,
	                help='SVD iterations. Default is 20.')

    return parser.parse_args()
