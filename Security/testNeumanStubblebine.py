from ahc.Ahc import ComponentModel, ComponentRegistry, ConnectorTypes,Event, EventTypes, Topology
from ahc.Channels.Channels import Channel
from ahc.Security.AKA.NeumanStubblebine import *
from cryptography.fernet import Fernet
import networkx
import os
import json
import time


def main():
    topology=Topology()

    alice_trent_key=Fernet.generate_key()
    bob_trent_key=Fernet.generate_key()

    topology.nodes["Alice"]=Alice("Alice", 0, alice_trent_key)
    topology.nodes["Bob"]=Bob("Bob", 1, bob_trent_key)
    topology.nodes["Trent"]=Trent("Trent", 2, alice_trent_key, bob_trent_key)

    topology.channels["Alice-Trent"]=Channel("Alice-Trent",3)
    topology.channels["Bob-Trent"]=Channel("Bob-Trent",4)
    topology.channels["Alice-Bob"]=Channel("Alice-Bob",5)

    topology.nodes["Trent"].connect_me_to_channel(ConnectorTypes.DOWN,topology.channels["Alice-Trent"])
    topology.nodes["Alice"].connect_me_to_channel(ConnectorTypes.UP,topology.channels["Alice-Trent"])

    topology.nodes["Trent"].connect_me_to_channel(ConnectorTypes.UP,topology.channels["Bob-Trent"])
    topology.nodes["Bob"].connect_me_to_channel(ConnectorTypes.DOWN,topology.channels["Bob-Trent"])

    topology.nodes["Alice"].connect_me_to_channel(ConnectorTypes.DOWN,topology.channels["Alice-Bob"])
    topology.nodes["Bob"].connect_me_to_channel(ConnectorTypes.UP,topology.channels["Alice-Bob"])

    topology.G=networkx.Graph()

    topology.G.add_node("Alice")
    topology.G.add_node("Bob")
    topology.G.add_node("Trent")

    topology.G.add_edge("Alice","Trent")
    topology.G.add_edge("Bob","Trent")
    topology.G.add_edge("Alice","Bob")

    topology.start()

    while True:
        pass

if __name__ == "__main__":
    main()