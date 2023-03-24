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

import socket
import struct

can_frame_fmt = "=IB3x8s";
can_frame_size = struct.calcsize (can_frame_fmt)

def dissect_can_frame(frame):
    can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame) 
    return (can_id, can_dlc, data[:can_dlc])

s = socket.socket (socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(("can1",))

while True:
    cf, addr = s.recvfrom(16)
    can_id = dissect_can_frame(cf)[0]
    if can_id == 165 :
        can_dlc = dissect_can_frame(cf)[1]
        dataL = hex((dissect_can_frame(cf)[2])[0])#Data LSB
        dataH = hex((dissect_can_frame(cf)[2])[1])#Data HSB
   
        #data= (int (dataH,16))<<8| int (dataL,16)
        data = int (dataH,16) + int (dataL,16)

        #print (dataL)
        #print(dataH )
        print (data)