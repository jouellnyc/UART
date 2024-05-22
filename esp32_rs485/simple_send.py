import time
from uart_conf import uart, de_pin, me

#Send 
de_pin.value(1)

count=0

while True:
    try:
        msg=f"hi from {me} at {time.localtime()}\n".encode()
        print(f"Sending  {msg}")
        uart.write(msg)
    except KeyboardInterrupt:
        print(f"Send {count} messages")
    else:
        count+=1
    finally:
        print(f"Send final {count} messages")
    time.sleep(1)    
