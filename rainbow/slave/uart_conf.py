import machine
import time

# Configure ESP32 pins (replace with actual pins you're using)
tx_pin = 7
rx_pin = 6
uart = machine.UART(2, baudrate=9600, tx=tx_pin, rx=rx_pin)
me="esp-02"  


