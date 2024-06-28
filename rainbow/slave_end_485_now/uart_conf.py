import machine

tx_pin1 = 7
rx_pin1 = 6
de_pin = machine.Pin(4, machine.Pin.OUT)
uart_rs485 = machine.UART(1, baudrate=9600, tx=tx_pin1, rx=rx_pin1)

#tx_pin2 = 10
#rx_pin2 = 3
uart_rs232 = None


