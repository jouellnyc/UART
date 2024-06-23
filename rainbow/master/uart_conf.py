import machine
import time

# Configure ESP32 pins (replace with actual pins you're using)
tx_pin = 17
rx_pin = 18
uart = machine.UART(2, baudrate=9600, tx=tx_pin, rx=rx_pin)
me="esp-01"  


