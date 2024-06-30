import time
from rgb_lib import set_color
from oled_setup import oled, show_rgb_text
from uart_lib import get_tuple_from_uart, send_tuple_using_uart

while True:
    
    """ Get the Tuple / Update the Display /  Send the Tuple """
    rgb_tuple = get_tuple_from_uart('rs232')
    
    if rgb_tuple:
        print(f"=={rgb_tuple}==")
        set_color(*rgb_tuple)
        time.sleep(1)
        show_rgb_text(rgb_tuple)
        send_tuple_using_uart('rs485', rgb_tuple)
    else:
        print('no data ', time.localtime())
        time.sleep(1)
    
    