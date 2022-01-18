import os
import sys
sys.path.insert(0, os.getcwd())
from ahc.Ahc import ComponentModel, Event, ConnectorTypes, Topology, EventTypes
from ahc.Ahc import ComponentRegistry
from cryptography.fernet import Fernet
import json
from enum import Enum
from datetime import date, datetime
import time
from ahc.Channels.Channels import Channel
import networkx as nx
import matplotlib.pyplot as plt
from ahc.Security.AKA.NeedhamSchroederSecure import *

          
"""
Topology here is manually created instead of using already existing functions. This was done due to existing functions only accepting one ComponentModel type for nodes of the topology.
"""
def main():
    topo = Topology()

    Key_A = Fernet.generate_key()
    Key_B = Fernet.generate_key()

    topo.nodes["T"] = Trent("Trent", 0, Key_A, Key_B)
    topo.nodes[A] = Alice(alice_componentname, 1, Key_A)
    topo.nodes[B] = Bob(bob_componentname, 2, Key_B)
    
    topo.channels["T-" + A] = Channel("T-" + A, 3)
    topo.nodes["T"].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels["T-" + A])
    topo.nodes[A].connect_me_to_channel(ConnectorTypes.UP, topo.channels["T-" + A])
    topo.channels[A + "-" + B] = Channel(A + "-" + B, 4)
    topo.nodes[A].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels[A + "-" + B])
    topo.nodes[B].connect_me_to_channel(ConnectorTypes.UP, topo.channels[A + "-" + B])
    topo.G = nx.Graph()
    topo.G.add_node("T")
    topo.G.add_node(A)
    topo.G.add_node(B)
    topo.G.add_edge("T", A)
    topo.G.add_edge(A, B)

    nx.draw(topo.G, with_labels=True, font_weight='bold')
    plt.draw()
    
    print(f'Starting topology, timestamp: {time.time()}')
    topo.start()
    # while True: pass
    plt.show()
    

if __name__ == "__main__":
    main() 