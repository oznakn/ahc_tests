"""Mutual Authentication using Interlock Protocol"""

import sys, os
import os
import sys

from networkx import algorithms

from ahc.Channels.Channels import Channel, P2PFIFOPerfectChannel

sys.path.insert(0, os.getcwd())

from ahc.Ahc import ComponentModel, Event, ConnectorTypes, Topology, EventTypes
from ahc.Ahc import ComponentRegistry
from enum import Enum
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import networkx, itertools, matplotlib.pyplot
from ahc.Security.AKA.Interlock import *
          
def main():
    pA = os.urandom(password_size)
    pB = os.urandom(password_size)
    digest = hashes.Hash(hashes.SHA256())
    digest.update(pA)
    hA = digest.finalize()
    digest = hashes.Hash(hashes.SHA256())
    digest.update(pB)
    hB = digest.finalize()
    topo = Topology()
    topo.nodes["Alice"] = Alice("Alice", 0, hA, hB, pA)
    topo.nodes["Bob"] = Bob("Bob", 1, hA, hB, pB)
    topo.channels["A-B"] = Channel("A-B", 2)
    topo.nodes["Alice"].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels["A-B"])
    topo.nodes["Bob"].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels["A-B"])
    topo.G = networkx.Graph()
    if isinstance(topo.G, networkx.Graph):
        topo.G.add_nodes_from(["Alice","Bob"])
        pairs = [["Alice", "Bob"]]
        topo.G.add_edges_from(pairs)
        networkx.draw(topo.G, with_labels= True, node_size = 1000)
        matplotlib.pyplot.draw()
        
    topo.start()
    
    #matplotlib.pyplot.savefig('plot.png')
    matplotlib.pyplot.show()
    while True: pass
    
if __name__ == '__main__':
    main()