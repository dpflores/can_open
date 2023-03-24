import canopen
import time


class CANOPEN():
    def __init__(self, port='can1', node_id=10, speed0=0):
        network = canopen.Network()
        network.connect(bustype='socketcan', channel=port)
        self.node = network.add_node(node_id, 'JD2xxx_v1.0.eds')
        

    def get_raw_data(self, hex):
        data = self.node.sdo[hex].raw 
        return data

   




