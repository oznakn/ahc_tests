from ahc.Ahc import Topology
from ahc.Channels.Channels import Channel
from ahc.Security.AKA.PublicKeyAuth import *


def main():
    topology = Topology()
    topology.construct_sender_receiver(HostNode,AliceNode,Channel)
    topology.start()

    while True: pass

if __name__ == "__main__":
    main()





