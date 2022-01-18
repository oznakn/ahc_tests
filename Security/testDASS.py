from ahc.Ahc import ComponentModel, Event, ConnectorTypes, EventTypes, Topology
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import time
import sys
import os
from ahc.Channels.Channels import Channel
from ahc.Security.AKA.DASS import *

import json

def main():
    topo = Topology()
    topo.construct_sender_receiver(Node1, Node2, Channel)
    topo.start()
    print("Type quit to exit chat")

    while True: pass


if __name__ == "__main__":
    main()
