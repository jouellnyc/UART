import time
from oled_setup import oled, show_rgb_text
from rgb_lib import set_color
from uart_lib import get_tuple_from_uart, send_tuple_using_uart

while True:
    """Get the Tuple / Update the Display / Send the Tuple"""
    rgb_tuple = get_tuple_from_uart("rs232")
    if rgb_tuple:
        print(f"== GOT {rgb_tuple}===")
        print(f"==Setting Color on Oled ==")
        set_color(*rgb_tuple)
        print(f"==Setting Color on RGB led ==")
        show_rgb_text(rgb_tuple)
        print(f"==sleeping 1 sec ==")
        time.sleep(1)
    else:
        print("No data at ", time.localtime())
        time.sleep(1)


    