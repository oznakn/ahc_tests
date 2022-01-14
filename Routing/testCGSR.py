import os
import sys
import random

sys.path.insert(0, os.getcwd())

import networkx as nx
import matplotlib.pyplot as plt

from ahc.Channels.Channels import P2PFIFOPerfectChannel,Channel
from ahc.Ahc import  Topology
from ahc.Ahc import ComponentRegistry
from ahc.Routing.CGSR.CGSRNode import CGSRNode

registry = ComponentRegistry()

def main():

  G = nx.random_geometric_graph(5, 0.5)
  topo = Topology()
  topo.construct_from_graph(G, CGSRNode, P2PFIFOPerfectChannel)
  nx.draw(G, with_labels=True, font_weight='bold')
  plt.draw()
  # for ch in topo.channels:
  #   topo.channels[ch].setPacketLossProbability(random.random())
  #   topo.channels[ch].setAverageNumberOfDuplicates(0)

  ComponentRegistry().print_components()

  topo.start()
    # while (True): pass
  topo.plot()
  plt.show()
  print(topo.nodecolors)
  for component in registry.components:
    print(component)


if __name__ == "__main__":
  main()
