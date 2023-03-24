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

# Escucha de los mensajes en el bus
while True:
    message = bus.recv()
    print(message)