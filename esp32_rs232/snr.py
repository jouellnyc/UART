
""" Simple Send and Receive """

import time
import machine

board_id = "esp-1\n"  # Replace with your desired board ID
from uart_conf import uart

while True:
    
    time.sleep(.5)
    uart.write(f"hello from {board_id}".encode())
    
    time.sleep(.5)
    rx_data = uart.readline()
    
    if rx_data:
        try:
            print(f"Received: {rx_data.decode()} - {time.localtime()}")
        except UnicodeError:
            print(f"Received: {rx_data.hex()} - {time.localtime()}")

