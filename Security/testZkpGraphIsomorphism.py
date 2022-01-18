import os
import sys
import random
import time
from enum import Enum

import networkx as nx

sys.path.insert(0,os.getcwd())

from ahc.Ahc import ComponentModel, Event, ConnectorTypes, Topology, EventTypes, ComponentRegistry
from ahc.Ahc import GenericMessageHeader, GenericMessagePayload, GenericMessage
from ahc.Channels.Channels import P2PFIFOPerfectChannel
from ahc.LinkLayers.GenericLinkLayer import LinkLayer
from ahc.Routing.AllSeeingEyeNetworkLayer import AllSeingEyeNetworkLayer
from ahc.Security.ZKP.ZkpGraphIsomorpishm import *
def main():

    topo = Topology()
    topo.construct_sender_receiver(NodePeggy, NodeVictor, P2PFIFOPerfectChannel)
    topo.start()

    while True: pass

if __name__ == "__main__":
  main()