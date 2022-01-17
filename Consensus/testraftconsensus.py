import time
import os
import sys

sys.path.insert(0, os.getcwd())
import networkx as nx

from ahc.Ahc import Topology
from ahc.Ahc import ComponentRegistry
from ahc.Channels.Channels import BasicLossyChannel
from ahc.Consensus.Raft.raft_component import RaftConsensusComponent
from itertools import combinations

registry = ComponentRegistry()

class Client:

    def send(self, message):
        print(tuple(message))


def main():
    nodes = ['A', 'B', 'C', 'D', 'E']

    edges = combinations(nodes, 2)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    topo = Topology()
    topo.construct_from_graph(G, RaftConsensusComponent, BasicLossyChannel)
    client = Client()

    topo.start()
    time.sleep(3)
    a_node: RaftConsensusComponent = topo.nodes.get('A')
    cluster = a_node.registry.get_non_channel_components()
    a_node = topo.nodes.get(cluster[0].state.leaderId)
    for i in range(10):
        a_node.data_received_client(client, {'type':'append',  'data': {
                                      'key': i,
                                      'value': 'hello + '+str(i),}})
        time.sleep(0.1)
    #waitforit = input("hit something to exit...")
    cnt = 1
    while True:
        cnt = cnt +1 
        time.sleep(1)
        if cnt > 5:
            break


if __name__ == "__main__":
    main()
