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

# create a bus instance using 'with' statement,
# this will cause bus.shutdown() to be called on the block exit;
# many other interfaces are supported as well (see documentation)
with can.Bus(interface='socketcan',
              channel='can0',
              receive_own_messages=True) as bus:

   # send a message
   message = can.Message(arbitration_id=123, is_extended_id=True,
                         data=[0x11, 0x22, 0x33])
   bus.send(message, timeout=0.2)

   # iterate over received messages
   for msg in bus:
       print(f"{msg.arbitration_id:X}: {msg.data}")

   # or use an asynchronous notifier
   notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])