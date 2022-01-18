import os
import datetime
import sys
import os
from time import sleep

from cryptography.hazmat.primitives import hashes
from ahc.Ahc import ComponentModel, Event, ConnectorTypes, Topology, EventTypes, GenericMessage, GenericMessageHeader
from ahc.Ahc import ComponentRegistry
from ahc.Ahc import EventTypes, ConnectorList, MessageDestinationIdentifiers
from ahc.Ahc import Event
from ahc.Channels.Channels import P2PFIFOPerfectChannel, Channel
from ahc.Security.AKA.OWALockoutSlowdown import *

sys.path.insert(0, os.getcwd())
registry = ComponentRegistry()

# USAGE:
# Register <username> <password> => Creates a new user
# Login <username> <password> => Authenticates the user, prints hash comparison for testing purposes
# Print => Lists registered users' hashes and salts
# Different from oneWayAuth.py, 5 wrong password locks alice out, restart the program.
# Also adaptive slowdown is implemented.


def main():
    topo = Topology();
    topo.construct_sender_receiver(Alice, Bob, Channel)
    topo.start()

    while True: pass


if __name__ == "__main__":
    main()
