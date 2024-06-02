import machine
import time

# Configure ESP32 pins (replace with actual pins you're using)
tx_pin = 13 
rx_pin = 14  

uart = machine.UART(2, baudrate=9600, tx=tx_pin, rx=rx_pin)
# Your Device's 'name'
me="esp-XXX"
