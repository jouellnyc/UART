import time
from uart_conf import uart, de_pin, me
    
#Receive
de_pin.value(0)
    
while True:
    print(uart.readline())
    time.sleep(1)    