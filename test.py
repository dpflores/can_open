from can_open import *


#CAN
port = 'can0'
id = 10
can_open = CANOPEN(port, id)    


while True:
    data = can_jd.get_raw_data(0x3403)
    print(f"data: {data}")




