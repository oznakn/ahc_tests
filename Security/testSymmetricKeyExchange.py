import os
import sys
sys.path.insert(0, os.getcwd())
from ahc.Ahc import ComponentModel, Event, ConnectorTypes, Topology, EventTypes
from cryptography.fernet import Fernet
from ahc.Channels.Channels import Channel
from ahc.Security.AKA.SymmetricKeyExchange import *

import networkx as nx
from time import sleep

"""    -----Schneier 3.1. Key Exchange: Key Exchange with Symmetric Cryptography------
    The protocol is as follows: Alice wants to communicate with Bob through a secure channel.
    Alice asks Trent(The Trusted 3rd Party) for a session key. Trent already shares secret
    keys with both Alice and Bob. Trent generates a session key for Alice and Bob and makes
    two copies of it. Encrypts one with Alice's the other with Bob's secret key, then
    sends both copies to Alice. Alice decrypts her copy and sends Bob his. Bob decrypts his copy
    and they both obtain the same session key in a secure way. Now they can communicate!
    The implementation also includes a pair message exchange after the key exchange for
    testing purposes.


    Generate Alice and Bob's secret keys that are shared with Trent"""

def Main():
    topo = Topology()

    """Create the Graph"""
    G = nx.Graph()
    G.add_node("Alice")
    G.add_node("Bob")
    G.add_node("Trent")
    G.add_edge("Alice", "Bob")
    G.add_edge("Trent", "Alice")

    """Create the Nodes and add them to the topology"""

    topo.G = G
    alice  = Alice("Alice", 0)
    bob = Bob("Bob", 1)
    trent = Trent("Trent", 2)
    topo.nodes["Alice"] = alice
    topo.nodes["Bob"] = bob
    topo.nodes["Trent"] = trent

    """Connect the Nodes through channels"""

    AB = Channel("AB", 3)
    AT = Channel("AT", 4)
    topo.channels["AB"] = AB
    alice.connect_me_to_channel(ConnectorTypes.DOWN, AB)
    bob.connect_me_to_channel(ConnectorTypes.DOWN, AB)
    topo.channels["AT"] = AT
    alice.connect_me_to_channel(ConnectorTypes.UP, AT)
    trent.connect_me_to_channel(ConnectorTypes.UP, AT)

    nx.draw(topo.G, with_labels=True, font_weight='bold')
  

    topo.start()
    sleep(10)
    print("---Communication End---")

if __name__ == "__main__":
    Main()
