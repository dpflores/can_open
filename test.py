from can_open import *


# #CAN
# port = 'can0'
# id = 165
# can_open = CANOPEN(port, id)    


# while True:
#     speed = can_jd.get_speed_stimation()
#     print(f"velocidad: {speed} m/s")


import canopen

network = canopen.Network()

# This will attempt to read an SDO from nodes 1 - 127
network.scanner.search()
# We may need to wait a short while here to allow all nodes to respond
time.sleep(0.05)
for node_id in network.scanner.nodes:
    print("Found node %d!" % node_id)