
""" Simple Send and Receive """

import time
import machine

from uart_conf import uart, me

while True:
    
    time.sleep(.5)
    uart.write(f"hello from {me}".encode())
    
    time.sleep(.5)
    rx_data = uart.readline()
    
    if rx_data:
        try:
            print(f"Received: {rx_data.decode()} - {time.localtime()}")
        except UnicodeError:
            print(f"Received: {rx_data.hex()} - {time.localtime()}")

