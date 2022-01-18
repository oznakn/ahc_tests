from enum import Enum
from time import time, sleep

import networkx

from ahc.Ahc import ComponentModel, Event, EventTypes, GenericMessageHeader, GenericMessage, Topology, ConnectorTypes
import hashlib
from secrets import SystemRandom
from ahc.Security.BitCommitmentOWF import *
from ahc.Channels.Channels import Channel

def main():
    topology = Topology()
    sender = Alice("Alice", 0)
    receiver = Bob("Bob", 1)
    channel = Channel("Channel", "0-1")
    graph = networkx.Graph()
    graph.add_nodes_from([0, 1])
    graph.add_edges_from([(0, 1)])
    topology.G = graph
    topology.nodes[sender.componentinstancenumber] = sender
    topology.nodes[receiver.componentinstancenumber] = receiver
    topology.channels[channel.componentinstancenumber] = channel
    sender.connect_me_to_channel(ConnectorTypes.DOWN, channel)
    receiver.connect_me_to_channel(ConnectorTypes.DOWN, channel)
    topology.start()
    sleep(10)


if __name__ == "__main__":
    main()
