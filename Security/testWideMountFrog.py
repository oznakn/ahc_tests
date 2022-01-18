import os
import sys

sys.path.insert(0, os.getcwd())

from ahc.Ahc import Topology
from ahc.Security.AKA.WideMouthFrog import Node


def main():
  topo = Topology()
  topo.construct_single_node(Node, 0)
  topo.start()
  while True: pass

if __name__ == "__main__":
  main()