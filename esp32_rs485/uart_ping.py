# uart_ping - simple UART ping to simulate Full Duplex and record RTT

import time
from uart_conf import uart, de_pin, me
msg='ping'
print(f"msg: {msg}")

#Send 
de_pin.value(1)
time.sleep(.0005)

start_time = time.ticks_ms()

try:
    uart.write(msg)
except Exception as e:
    print(f"Sent {msg} NOTOK {e}")

"""
# Without the next sleep the receiver gets too much noise and will receive something like 'b\xfe'.
# I.E The system did not have a chance to receive the data yet so we can't change voltage to receive
# immediately after sending! -- 4ms is about the lowest that mostly works, so we can mostly use 5 ms.

# However, set it too high and the receiver has now become a sender and you have missed the data
# because you have not become a receiver yet. :D

# Min is 5ms
# Max is 15ms
"""
time.sleep(.005)

#Receive
de_pin.value(0)

"""
This value can be much lower - flipping the voltage on the GPIO takes a very small amount of time).
We set it to 0.5 ms. YMMV.
"""
time.sleep(.0005)

while True:
    
    """ 5 ms """
    time.sleep(.005)
    msg=uart.readline()
    
    if msg:
        end_time = time.ticks_ms()
        execution_time_ms = (end_time - start_time)  
        print(f"Got {msg.decode()} back in {execution_time_ms} ms ")   
    
