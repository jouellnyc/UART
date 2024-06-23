import time

from rgb_pins_config import red_pwm, green_pwm, blue_pwm
from rgb_lib import set_color

from oled_setup import oled, clear, show_rgb_text

from uart_lib import uart_send,uart_receive  
from uart_conf import uart

"""
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
"""

from rainbow_gen_ind  import rainbow_generator

delay=.25
color_gen = rainbow_generator(step_size=35)

while True:
    
    r = next(color_gen)
    g = next(color_gen)
    b = next(color_gen)
    first_rgb = (r,g,b)
    
    r2 = next(color_gen)
    g2 = next(color_gen)
    b2 = next(color_gen)
    next_rgb=(r2,g2,b2)
    
    uart_send(uart,bytes(next_rgb))
    
    set_color(*first_rgb)
    clear()
    print(first_rgb)
    show_rgb_text(first_rgb)
    time.sleep(delay)
    
    ##not sure what do here yet
    clear()
    print(next_rgb)
    show_rgb_text(next_rgb)
    time.sleep(delay)   
    
    
    
