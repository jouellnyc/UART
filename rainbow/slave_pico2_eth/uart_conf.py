import machine
from machine import Pin

tx_pin0 = 4
rx_pin0 = 5
#uart_rs232 = machine.UART(1, baudrate=9600, tx=Pin(tx_pin0), rx=Pin(rx_pin0, pull=Pin.PULL_UP))
#uart_rs232 = machine.UART(1, baudrate=9600, tx=tx_pin0, rx=rx_pin, pull=Pin.PULL_UP)
uart_rs232 = machine.UART(1, baudrate=9600, tx=tx_pin0, rx=rx_pin0)

#uart = UART(1, baudrate=38400, bits=8, parity=None, stop=1, timeout_char=10, tx=Pin(4), rx=Pin(5, pull=Pin.PULL_UP), rxbuf=49, invert=0, timeout=10, txbuf=49, flow=0)

"""
tx_pin2 = 7
rx_pin2 = 6
de_pin = machine.Pin(9, machine.Pin.OUT)
uart_rs232 = machine.UART(1, baudrate=9600, tx=tx_pin2, rx=rx_pin2)
"""

uart_rs485 = None

