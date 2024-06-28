import time

from rgb_pins_config import red_pwm, green_pwm, blue_pwm
from rgb_lib import set_color

from oled_setup import oled, clear, show_rgb_text

from uart_lib import uart_send,uart_receive  
from uart_conf import uart


from rainbow_gen_ind  import rainbow_generator

delay=.1
color_gen = rainbow_generator(step_size=5)

while True:
    
    r = next(color_gen)
    g = next(color_gen)
    b = next(color_gen)
    first_rgb = (r,g,b)
    set_color(*first_rgb)
    print(first_rgb)
    time.sleep(delay)
    
    
    
    

