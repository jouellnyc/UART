import time
from uart_conf import uart_rs232, uart_rs485

verbose=True

def encode_rgb_tuple_to_bytes(data):
    packed_data  = ','.join(str(value) for value in data) + '\n'
    encoded_data = packed_data.encode('utf-8')
    return encoded_data
    
class Rs485Uart:
    """Initialize Rs485Uart object with uart_rs485, de_pin, and sleep_time"""
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
        self.de_pin.value(1)
        time.sleep(self.sleep_time)
        encoded_data = encode_rgb_tuple_to_bytes(rgb_tuple)
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
        encoded_data = encode_rgb_tuple_to_bytes(rgb_tuple)
        time.sleep(self.sleep_time)
        return self.uart.write(encoded_data)

uart_classes = {
    'rs485': Rs485Uart,
    'rs232': Rs232Uart
}


"""Get a UART instance based on the given type"""
def get_uart_instance(uart_type):
    if uart_type == 'rs232':
        return Rs232Uart(uart_rs232, sleep_time=0.1)
    elif uart_type == 'rs485':
        from uart_conf import de_pin
        return Rs485Uart(uart_rs485, de_pin, sleep_time=0.1)
    else:
        raise ValueError('Invalid uart type')

"""
Gets a valid RGB tuple from the UART port, retrying once if needed.
Decode bytes to string and split by comma,  Convert each string value to integer and create tuple

NOTE:
>>> tuple(int(value) for value in ['255', '255', '0\n'])
  (255, 255, 0)

Returns:
    tuple: A valid RGB tuple (0, 0, 0) to (255, 255, 255), or None if data is invalid or not received.
"""

    
def decode_and_split_data_from_uart(data):
    """ Returns a list of integers after decoding and splitting data """
    try:
        rgb_values = [int(val) for val in data.decode().split(',')]
    except (ValueError, UnicodeError):
            print(f"Failed to convert received data: {data}")
            return None
    else:
        return rgb_values

    
def data_from_uart_is_valid(data):
    if all(0 <= val <= 255 for val in data):
        
        if len(data) == 3:
            return True
        else:
            print(f"Invalid number of values received: {len(data)} (expected 3)")
            return None
    else:
        print(f"Invalid RGB values: {data.decode()}")
        return None
        

def get_tuple_from_uart(uart_type):
    myuart = get_uart_instance(uart_type)
    _rgb = myuart.uart_receive()
    if _rgb:
        if verbose:
            print(f"Raw UART Lib got {_rgb}")
        rgb_list=decode_and_split_data_from_uart(_rgb)
        if rgb_list:
            if verbose:
                print(f"Rgb_list: {rgb_list}")
            if data_from_uart_is_valid(rgb_list):
                rgb_values = tuple(rgb_list)
                if verbose:
                    print(f"rgb_values: {rgb_values}")
                return rgb_values
            else:
                return None
        else:
            return None
    else:
        return None

"""Send a tuple to the UART"""
def send_tuple_using_uart(uart_type, rgb_tuple):
    myuart = get_uart_instance(uart_type)
    myuart.uart_send(rgb_tuple)

