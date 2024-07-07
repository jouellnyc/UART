import machine
import time

tx_pin1 = 17
rx_pin1 = 18
uart_rs232 = machine.UART(2, baudrate=19200, tx=tx_pin1, rx=rx_pin1)

#Master only uses rs232, but libary imports both
uart_rs485=None