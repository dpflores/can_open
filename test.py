from can_open import *


# #CAN
# port = 'can0'
# id = 165
# can_open = CANOPEN(port, id)    


# while True:
#     speed = can_jd.get_speed_stimation()
#     print(f"velocidad: {speed} m/s")


import can

# Configuración del bus CAN
bus = can.interface.Bus(channel='can1', bustype='socketcan')

# Envío de un mensaje con ID (HEX) A5 y DLC de 5 bytes
msg = can.Message(arbitration_id=0xA5, data=[0x11, 0x22, 0x33, 0x44, 0x55])
bus.send(msg)

# Lectura del primer byte del mensaje con ID (HEX) A5
while True:
    message = bus.recv()
    if message.arbitration_id == 0xA5 and message.dlc == 5:
        first_byte = message.data[0]
        print(f"El primer byte del mensaje CAN con ID (HEX) A5 es: {first_byte}")
        break