import time
from uart_conf import uart_rs232, uart_rs485

class Rs485Uart:
    """Initialize Rs485Uart object with uart_rs485, de_pin, and sleep_time"""
    """If you are using Rs485 you need to define it's depin and uart in uart.conf """
    def __init__(self, uart_rs485, de_pin, sleep_time):
        self.uart = uart_rs485
        self.de_pin = de_pin
        self.sleep_time = sleep_time
        
    """Receive data from UART"""
    def uart_receive(self):
        self.de_pin.value(0)
        time.sleep(self.sleep_time)
        return self.uart.readline()
    
    """Send data to UART"""
    def uart_send(self, rgb_tuple):
        encoded_data = ','.join(str(value) for value in rgb_tuple).encode('utf-8')
        self.de_pin.value(1)
        time.sleep(self.sleep_time)
        return self.uart.write(encoded_data)

class Rs232Uart:
    """Initialize Rs232Uart object with uart_rs232 and sleep_time"""
    def __init__(self, uart_rs232, sleep_time):
        self.uart = uart_rs232
        self.sleep_time = sleep_time
        
    """Receive data from UART"""
    def uart_receive(self):
        return self.uart.readline()
    
    """Send data to UART"""
    def uart_send(self, rgb_tuple):
        encoded_data = ','.join(str(value) for value in rgb_tuple).encode('utf-8')
        time.sleep(self.sleep_time)
        return self.uart.write(encoded_data)

uart_classes = {
    'rs485': Rs485Uart,
    'rs232': Rs232Uart
}

"""Convert bytes to a tuple of RGB values"""
def bytes_to_rgb_tuple(byte_string):
    """Decode bytes to string and split by comma
    Convert each string value to integer and create tuple"""
    rgb_str = byte_string.decode('utf-8').split(',')
    return tuple(int(value) for value in rgb_str)
    
    
"""Get a UART instance based on the given type"""
def get_uart_instance(uart_type):
    if uart_type == 'rs232':
        return Rs232Uart(uart_rs232, sleep_time=0.1)
    elif uart_type == 'rs485':
        from uart_conf import de_pin
        return Rs485Uart(uart_rs485, de_pin, sleep_time=0.1)
    else:
        raise ValueError('Invalid uart type')
    
"""Get a tuple from the UART"""
def get_tuple_from_uart(uart_type):
    myuart = get_uart_instance(uart_type)
    _rgb = myuart.uart_receive()
    if _rgb:
        print(_rgb)
        return bytes_to_rgb_tuple(_rgb)
    else:
        return None
    
"""Send a tuple to the UART"""
def send_tuple_using_uart(uart_type, rgb_tuple):
    myuart = get_uart_instance(uart_type)
    myuart.uart_send(rgb_tuple)

