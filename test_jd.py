from can_open import *


#CAN
port = 'can0'
id = 165
can_open = CANOPEN(port, id)    


while True:
    speed = can_jd.get_speed_stimation()
    print(f"velocidad: {speed} m/s")


