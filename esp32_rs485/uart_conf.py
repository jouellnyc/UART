import machine
import time

# Configure ESP32 pins (replace with actual pins you're using)
tx_pin = 13  # Typically connected to DE and TxD of MAX485
rx_pin = 14  # Typically connected to RE and RxD of MAX485
uart = machine.UART(2, baudrate=9600, tx=tx_pin, rx=rx_pin)
de_pin = machine.Pin(4, machine.Pin.OUT)
me="esp-XXX"
    
