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

import can

# Definir la interfaz de red CAN
can_interface = 'can0'

# Crear un bus CAN
bus = can.interface.Bus(can_interface, bustype='socketcan_native')

# Definir el ID del mensaje a buscar (A5 en hexadecimal)
message_id = 0xA5

# Leer los mensajes del bus CAN y filtrar por ID
while True:
    message = bus.recv()
    if message.arbitration_id == message_id:
        print('Datos recibidos: {}'.format(message.data.hex()))