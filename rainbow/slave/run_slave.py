import time
from rgb_lib import set_color
from oled_setup import oled, clear, stext
from uart_lib import uart_send,uart_receive,bytes_to_rgb_tuple  
from uart_conf import uart

while True:
    _rgb=uart_receive(uart)
    if _rgb:
        print(_rgb)
        rgb=bytes_to_rgb_tuple(_rgb)
        r,g,b = rgb
        set_color(*rgb)
        clear()
        stext(   'R    G    B',27, 17)
        stext(str(rgb),      25, 37)
    time.sleep(.5)


