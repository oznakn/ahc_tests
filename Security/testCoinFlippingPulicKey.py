from ahc.Ahc import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import secrets
import string
import random
from time import sleep
from ahc.Channels.Channels import Channel
from enum import Enum
from cryptography.hazmat.primitives import serialization
from ahc.Security.CoinFlippingPublicKey import *
# Hakan Kanbur

def main():
    topology = Topology()
    topology.construct_sender_receiver(Alice, Bob, Channel)
    topology.start()
    sleep(4)
    #while (True): pass


if __name__ == "__main__":
    main()
