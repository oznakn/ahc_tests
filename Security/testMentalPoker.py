from ahc.Ahc import Topology, ConnectorTypes
from ahc.Channels.Channels import Channel

from time import time, sleep

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from ahc.Security.MentalPoker import *

from enum import Enum
import networkx
import string
import secrets
import random

def main():
    topo = Topology()
    alice = Alice("Alice",0)
    bob = Bob("Bob",1)
    carol = Carol("Carol",2)
    channel1 = Channel("Channel1", "0-1")
    channel2 = Channel("Channel2", "0-2")
    channel3 = Channel("Channel3", "1-2")
    graph = networkx.Graph()
    graph.add_nodes_from([0, 1, 2])
    graph.add_edges_from([(0, 1),(0, 2),(1, 2)])
    topo.G = graph
    topo.nodes[alice.componentinstancenumber] = alice
    topo.nodes[bob.componentinstancenumber] = bob
    topo.nodes[carol.componentinstancenumber] = carol
    topo.channels[channel1.componentinstancenumber] = channel1
    topo.channels[channel2.componentinstancenumber] = channel2
    topo.channels[channel3.componentinstancenumber] = channel3
    alice.connect_me_to_channel(ConnectorTypes.DOWN, channel1)
    alice.connect_me_to_channel(ConnectorTypes.DOWN, channel2)
    bob.connect_me_to_channel(ConnectorTypes.DOWN, channel1)
    bob.connect_me_to_channel(ConnectorTypes.DOWN, channel3)
    carol.connect_me_to_channel(ConnectorTypes.DOWN, channel2)
    carol.connect_me_to_channel(ConnectorTypes.DOWN, channel3)
    topo.start()
    sleep(10)


if __name__ == "__main__":
    main()
