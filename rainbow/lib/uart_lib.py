def uart_send(uart, data):
    encoded_data = ','.join(map(str, data)).encode('utf-8')
    uart.write(encoded_data)
    
def uart_receive(uart):
    return uart.read()

def bytes_to_rgb_tuple(byte_string):
    # Decode bytes to string and split by comma
    rgb_str = byte_string.decode('utf-8').split(',')
    # Convert each string value to integer and create tuple
    return tuple(int(value) for value in rgb_str)