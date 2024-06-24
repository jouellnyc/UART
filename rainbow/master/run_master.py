import time

from rgb_pins_config import red_pwm, green_pwm, blue_pwm
from rgb_lib import set_color

from oled_setup import oled, clear, show_rgb_text

from uart_lib import uart_send,uart_receive  
from uart_conf import uart

delay=2

colors=[
    (255, 0, 0),
    (255,15,0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255),
    (75, 0, 130),
    (143, 0, 255)
]

while True:
    
    for rgb in colors:
        
        set_color(*rgb)
        show_rgb_text(rgb)
        time.sleep(delay)
        uart_send(uart,bytes(rgb))
    