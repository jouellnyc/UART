import machine
import time

from uart_conf import uart_rs232 as uart
board_id = "esp-1"  # Replace with your desired board ID

while True:
    
    data = "hello from " + board_id
    uart.write(data.encode())
    print(f"Sent: {data}")
    time.sleep(3)  # Delay between transmissions

    rx_data = uart.read()
    if rx_data:
        print(f"Received: {rx_data.decode()}")