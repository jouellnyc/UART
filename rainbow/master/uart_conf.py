import machine
import time

# Configure ESP32 pins (replace with actual pins you're using)
tx_pin1 = 17
rx_pin1 = 18
uart_rs232 = machine.UART(2, baudrate=9600, tx=tx_pin1, rx=rx_pin1)

#tx_pin2 = 10
#rx_pin2 = 3
uart_rs485=None