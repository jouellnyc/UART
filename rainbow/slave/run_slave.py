import time
from rgb_lib import set_color
from oled_setup import oled, show_rgb_text
from uart_lib import get_tuple_from_uart

while True:
    rgb=get_tuple_from_uart()
    
    if rgb:
        print(f"=={rgb}==")
        set_color(*rgb)
        show_rgb_text(rgb)
    else:
        print('no data')
    time.sleep(1)