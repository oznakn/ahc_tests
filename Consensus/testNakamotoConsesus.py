
import sys
from copy import deepcopy
from enum import Enum

import networkx as nx
from random import choice

import matplotlib.pyplot as plt

from ahc.Channels.Channels import Channel
from ahc.Ahc import ComponentRegistry, Topology
from ahc.Consensus.NakamotoConsensus import transaction_generator, NkComponent

# TODO: Check if this is a valid implementation
PATH_OF_DATA = "data"
sys.setrecursionlimit(1500)

def main():
    number_of_nodes = 5
    number_of_txn = 50
    G = nx.erdos_renyi_graph(number_of_nodes, 0.4)
    transaction_generator(number_of_nodes,number_of_txn)
    topo = Topology()
    topo.construct_from_graph(G, NkComponent, Channel)

    ComponentRegistry().print_components()
    topo.start()
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

if __name__ == '__main__':
    main()
    while True: pass