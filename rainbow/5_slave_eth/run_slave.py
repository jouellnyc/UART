import time
from oled_setup import oled, show_rgb_text
from rgb_lib import set_color
from myipaddress import url
from www_cli import get_rgb_from_http

while True:
    rgb_tuple = get_rgb_from_http(url,verbose=True)
    if rgb_tuple:
        print(f"=={rgb_tuple}==")
        set_color(*rgb_tuple)
        show_rgb_text(rgb_tuple)
        #send_tuple_using_uart('rs232', rgb_tuple)
    else:
        print(f"No data")
    time.sleep(1)
    