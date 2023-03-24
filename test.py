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

import can

# Configuración del bus CAN
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Escucha de los mensajes en el bus
while True:
    message = bus.recv()
    print(f"ID: {message.arbitration_id}, DLC: {message.dlc}, Data: {message.data}")