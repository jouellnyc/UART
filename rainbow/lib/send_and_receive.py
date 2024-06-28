import machine
import time
from uart_conf import uartblah as uart,me

while True:
    
    data = "hello from " + me
    uart.write(data.encode())
    print(f"Sent: {data}")
    time.sleep(3)  # Delay between transmissions

    rx_data = uart.read()
    if rx_data:
        print(f"Received: {rx_data.decode()} at {time.localtime()}")




