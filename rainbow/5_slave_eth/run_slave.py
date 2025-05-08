import time
from oled_setup import oled, show_rgb_text
from rgb_lib import set_color
from myipaddress import url
from www_cli import get_rgb_from_http

while True:

    rgb_tuple = get_rgb_from_http(url + '/test/rgb/',verbose=True)
        
    if rgb_tuple:
        print(f"=={rgb_tuple}==")
        set_color(*rgb_tuple)
        show_rgb_text(rgb_tuple)
    else:
        show_rgb_text('None')
        set_color(255,0,0)
        print(f"No data at {time.localtime()}")
    time.sleep(1)       
