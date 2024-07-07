import time
time.sleep(5)
from colors import colors
from rgb_lib import set_color
from oled_setup import oled, show_rgb_text
from uart_lib import get_tuple_from_uart, send_tuple_using_uart
  
hold_led=1
wait_for_new=5
while True:
    
    for rgb_tuple in colors:
        
        print(f"===== {rgb_tuple} =====")
        print(f"==Setting Color on RGB led ==")
        set_color(*rgb_tuple)
        print(f"==Setting Color on Oled ==")
        show_rgb_text(rgb_tuple)
        print(f"==Sleeping for {hold_led} secs ==")
        time.sleep(hold_led)
        print(f"==Sending tuple * ==")
        send_tuple_using_uart('rs232', rgb_tuple)
        print(f"==Sleeping for {wait_for_new} secs ==")
    time.sleep(wait_for_new)