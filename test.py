from can_open import *


#CAN
port = 'can1'
id = 10
can_open = CANOPEN(port, id)    


# Para el JD2120
# while True:
#     data = can_open.get_raw_data(0x3403)
#     print(f"data: {data}")

while True:
    data = can_open.get_raw_data(0xA5)
    print(f"data: {data}")



