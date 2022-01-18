import os
import sys
import time
import random
import codecs
from enum import Enum
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import cmac

sys.path.insert(0, os.getcwd())
sys.path.insert(1, (os.path.join(os.getcwd(), "../")))

import networkx as nx
import matplotlib.pyplot as plt

from ahc.Ahc import ComponentModel, Event, ConnectorTypes, Topology
from ahc.Ahc import ComponentRegistry
from ahc.Ahc import GenericMessagePayload, GenericMessageHeader, GenericMessage, EventTypes
from ahc.Channels.Channels import P2PFIFOPerfectChannel
from ahc.LinkLayers.GenericLinkLayer import LinkLayer
from ahc.Routing.AllSeeingEyeNetworkLayer import AllSeingEyeNetworkLayer
from ahc.Security.AKA.SKID2 import *

def main():
    # create nodeAlice
    # create nodeBob
    topo = Topology()
    topo.construct_sender_receiver(Alice, Bob, P2PFIFOPerfectChannel)
    topo.start()

    #while(True):
    #    pass
    time.sleep(5)

if __name__ == "__main__":
    main()