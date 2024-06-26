import time
from colors import colors
from rgb_lib import set_color
from oled_setup import oled, show_rgb_text
from uart_lib import get_tuple_from_uart, send_tuple_using_uart
  
delay=2

while True:
    
    for rgb_tuple in colors:
        
        print(f"=={rgb_tuple}==")
        set_color(*rgb_tuple)
        show_rgb_text(rgb_tuple)
        time.sleep(delay)
        send_tuple_using_uart('rs232', rgb_tuple)