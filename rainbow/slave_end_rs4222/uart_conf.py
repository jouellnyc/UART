import machine

tx_pin1 = 10
rx_pin1 = 2
uart_rs485 = machine.UART(1, baudrate=9600, tx=tx_pin1, rx=rx_pin1)

tx_pin2 = 46
rx_pin2 = 3
de_pin = machine.Pin(9, machine.Pin.OUT)
uart_rs232 = machine.UART(2, baudrate=9600, tx=tx_pin2, rx=rx_pin2)

