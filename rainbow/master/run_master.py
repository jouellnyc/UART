import time

from rgb_pins_config import red_pwm, green_pwm, blue_pwm
from rgb_lib import set_color

from oled_setup import oled, clear, stext

from uart_lib import uart_send,uart_receive  
from uart_conf import uart

from rainbow_gen import rainbow_generator


def rainbow_transition(step_size=5, delay_secs=1):
    color_gen = rainbow_generator(step_size)
    while True:
        rgb_tuple = next(color_gen)
        set_color(*rgb_tuple)
        clear()
        print(rgb_tuple)
        stext(   'R    G    B' , 27, 17)
        stext(str(rgb_tuple),        25, 37)
        uart_send(uart,bytes(rgb_tuple))
        time.sleep(delay_secs)

rainbow_transition(step_size=10, delay_secs=1)