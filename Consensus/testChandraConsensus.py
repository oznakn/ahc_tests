from enum import Enum
from threading import Timer
from ahc.Ahc import Topology, ComponentModel, ConnectorTypes, ComponentRegistry
from ahc.Consensus.ChandraConsensus import ChandraChannel, ChandraComponents
import time
registry = ComponentRegistry()

class ChandraConsensusNode(ComponentModel):

    def __init__(self, componentname, componentid, numberofNodes=10):
        self.channel = ChandraChannel("ChandraChannel", 0)
        for n in range(0, numberofNodes):
            tComp = ChandraComponents("ChandraNode", n, numberofNodes)
            tComp.connect_me_to_channel(ConnectorTypes.DOWN, self.channel)
            registry.add_component(tComp)

        registry.get_component_by_key("ChandraNode", 0).set_as_coordinator()
        super().__init__(componentname, componentid)

def main():
    topo = Topology()
    topo.construct_single_node(ChandraConsensusNode, 0)
    topo.start()
    
    cnt = 1
    while True:
        cnt = cnt +1 
        time.sleep(1)
        if cnt > 10:
            break


if __name__ == '__main__':
    main()
