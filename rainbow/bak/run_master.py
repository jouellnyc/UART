import time

from rgb_pins_config import red_pwm, green_pwm, blue_pwm
from rgb_lib import set_color

from oled_setup import oled, clear, stext

from uart_lib import uart_send,uart_receive  
from uart_conf import uart

from rainbow import create_rainbow

rainbow_colors=create_rainbow()
while True:
    for color in rainbow_colors:
        set_color(*color)
        clear()
        print(color)
        stext(   'R    G    B' , 27, 17)
        stext(str(color),        25, 37)
        uart_send(uart,bytes(color))
        time.sleep(.5)       
        