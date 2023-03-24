# from can_open import *


# #CAN
# port = 'can1'
# id = 10
# can_open = CANOPEN(port, id)    


# # Para el JD2120
# # while True:
# #     data = can_open.get_raw_data(0x3403)
# #     print(f"data: {data}")

# while True:
#     data = can_open.get_raw_data(0x104)
#     print(f"data: {data}")

# import the library

from socket_can import *

# CAN configuration
can_id = 0x10
can_frame_fmt = "=IB3x8s"
can_port = "can0"

can = CAN(can_frame_fmt, can_port, can_id)

while True:
    print(can.get_vel(sender_id=0xA5))