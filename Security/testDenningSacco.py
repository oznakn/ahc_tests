import math
import struct

from ahc.Ahc import ComponentModel, Topology, Event, ConnectorTypes, EventTypes, ComponentRegistry
from ahc.Channels.Channels import Channel
from ahc.Security.AKA.DenningSacco import *

import time
import networkx as nx

def Main():
    topo: Topology = Topology()
    topo.nodes['A'] = Alice('Alice', 0)
    topo.nodes['B'] = Bob('Bob', 1)
    topo.nodes['T'] = Trent('Trent', 2)

    topo.channels['A-T'] = Channel('A-T', 3)
    topo.channels['A-B'] = Channel('A-B', 4)

    topo.nodes['T'].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels['A-T'])
    topo.nodes['A'].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels['A-T'])
    topo.nodes['A'].connect_me_to_channel(ConnectorTypes.UP, topo.channels['A-B'])
    topo.nodes['B'].connect_me_to_channel(ConnectorTypes.DOWN, topo.channels['A-B'])

    topo.G = nx.Graph()
    topo.G.add_nodes_from(['A', 'B', 'T'])
    topo.G.add_edges_from([('A', 'T'), ('A', 'B')])

    topo.start()
    #while True: pass
    time.sleep(10)

if __name__ == "__main__":
    Main()
