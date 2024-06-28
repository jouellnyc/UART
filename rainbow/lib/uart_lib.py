import time
from uart_conf import uart_rs232, uart_rs485


def bytes_to_rgb_tuple(byte_string):
        # Decode bytes to string and split by comma
        rgb_str = byte_string.decode('utf-8').split(',')
        # Convert each string value to integer and create tuple
        return tuple(int(value) for value in rgb_str)
    
class Rs485Uart:
    def __init__(self):
        self.flip_de_pin_sleep=.1
        self.uart = uart_rs485
        self.de_pin = de_pin
        
    def uart_receive(self):
        self.de_pin.value(0)
        time.sleep(self.flip_de_pin_sleep)
        return self.uart.read()
    
    def uart_send(self, data):
        encoded_data = ','.join(map(str, data)).encode('utf-8')
        self.de_pin.value(1)
        time.sleep(self.flip_de_pin_sleep)
        return self.uart.write(encoded_data)
    
        
class Rs232Uart:

    def __init__(self):
        self.sleep=.1
        self.uart = uart_rs232
        
    def uart_receive(self):
        return self.uart.read()
    
    def uart_send(self, data):
        encoded_data = ','.join(map(str, data)).encode('utf-8')
        time.sleep(self.sleep)
        return self.uart.write(encoded_data)

uart_classes = {
    'rs485': Rs485Uart,
    'rs232': Rs232Uart
}

def get_uart_instance(uart_type):
    if uart_type in uart_classes:
        return uart_classes[uart_type]()
    else:
        raise ValueError('Invalid uart type')
    
def get_tuple_from_uart(uart_type):
    myuart = get_uart_instance(uart_type)
    _rgb = myuart.uart_receive()
    if _rgb:
        print(_rgb)
        return bytes_to_rgb_tuple(_rgb)
    else:
        return None
    
def send_tuple_using_uart(uart_type, data):
    myuart = get_uart_instance(uart_type)
    myuart.uart_send(data)