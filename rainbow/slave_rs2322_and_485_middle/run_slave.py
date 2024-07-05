import time

from rgb_lib import set_color
from oled_setup import oled, show_rgb_text
from uart_lib import get_tuple_from_uart, send_tuple_using_uart


while True:
    """Get the Tuple / Update the Display / Send the Tuple"""
    """Allow 2 seconds for any line noise to clear at start up"""
    try:
        rgb_tuple = get_tuple_from_uart("rs232")
    except ValueError as e:
        if "invalid syntax for integer with base 10" in str(e):
            print("sleeping 2 secs")
            time.sleep(2)
    else:
        if rgb_tuple:
            print(f"==GOT {rgb_tuple}===")
            print(f"==Setting Color on Oled ==")
            set_color(*rgb_tuple)
            print(f"==Setting Color on RGB led ==")
            show_rgb_text(rgb_tuple)
            print(f"==sleeping 1 sec ==")
            time.sleep(1)
            print(f"== Sending {rgb_tuple}===")
            send_tuple_using_uart("rs485", rgb_tuple)
        else:
            print("no data", time.localtime())
            time.sleep(0.5)
