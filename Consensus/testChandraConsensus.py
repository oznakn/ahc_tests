from enum import Enum
from threading import Timer
from ahc.Ahc import Topology, ComponentModel, ConnectorTypes, ComponentRegistry
from ahc.Consensus.ChandraConsensus import ChandraChannel, ChandraComponents
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
    while True: pass


if __name__ == '__main__':
    main()
