import time
from oled_setup import oled, show_rgb_text, clear
from rgb_lib import set_color
from myipaddress import url
from www_cli import get_rgb_from_http

while True:

    print(f"== {time.localtime()}")
    rgb_tuple = get_rgb_from_http(url, verbose=False, timeout=3)
    if rgb_tuple:
        if rgb_tuple == (9,9,9):
            clear()
        else:
            print(f"=={rgb_tuple}==\n")
            set_color(*rgb_tuple)
            show_rgb_text(rgb_tuple)
    else:
        print(f"No data retrieved\n")
    time.sleep(1)       
