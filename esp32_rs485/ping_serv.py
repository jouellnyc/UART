# ping_serv - Send back what the Sender Sent

import time
from uart_conf import uart, de_pin, me
    
#Receive
de_pin.value(0)

while True:
    
    """ 5 ms """
    time.sleep(.005)
    msg=uart.readline()
    
    if msg:
        try:
            msg=msg.decode("utf-8")
        except UnicodeError:
            print(f"UnicodeError: {msg}")
        #Shave a few ms off if not debugging
        """
        else:
            print(f"Got {msg}")
        """
        #Send 
        de_pin.value(1)
        time.sleep(.0005)
        uart.write(msg)      
    
