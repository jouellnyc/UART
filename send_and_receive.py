import machine
import time
uart = machine.UART(2, baudrate=9600, tx=13, rx=14)
board_id = "esp-2"  # Replace with your desired board ID

while True:
    
    data = "hello from " + board_id
    uart.write(data.encode())
    print(f"Sent: {data}")
    time.sleep(3)  # Delay between transmissions

    rx_data = uart.read()
    if rx_data:
        print(f"Received: {rx_data.decode()}")



