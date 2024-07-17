import machine

tx_pin0 = 0
rx_pin0 = 1
uart_rs232 = machine.UART(0, baudrate=9600, tx=tx_pin0, rx=rx_pin0)

"""
tx_pin2 = 7
rx_pin2 = 6
de_pin = machine.Pin(9, machine.Pin.OUT)
uart_rs232 = machine.UART(1, baudrate=9600, tx=tx_pin2, rx=rx_pin2)
"""

uart_rs485 = None
