## Raspi Pico and SIM800L 

##  BackStory
My goal was to get a little bit more involved in Internet of Things From a cellular perspective, not spending a ton of money up front. To that end I did some research and it appeared that the SimCom sim800l module would be a perfect fit.  I went ahead and purchased five of these modules from AliExpress, knowing that a few of them weren't going to work. Sure enough three of them did not power up one of them had a bent SIM card holder but two of them did power up. 

##  Upfront lesson:
Always by at least two of the items from Ali Express

##  Spoiler Alert
This was a partial success. 


| Prerequisite | Details |
|---|---|
| Pi Pico |
|Sim800L| Anywhere on AliExpress| Just grab one|

![image](https://github.com/user-attachments/assets/2e2227dc-60cb-489f-9f6b-476d9e145e15)


## UART Pin Configuration

| Module | Pico |
|---|---|
| SIM800L TX | GPIO 01 |
| SIM800L RX | GPIO 00 |
| SIM800L GND | GND|

Pretty Straight Forward in terms of connections:

```
#gsmuart.py

import machine
import time
uart = machine.UART(0, baudrate=115200, tx=machine.Pin(0), rx=machine.Pin(1))
```

## Other Pins

| Module | Pico |
|---|---|
| SIM800L VCC | 5V |
| SIM800L GND | GND |


### Tips from Arduino Forum
```
You should be very careful to:

-  Disconnect VCC first
-  Connect    GND first

Otherwise, the module can use the low voltage serial pins as ground and can get destroyed instantly.
```

### Notes from Arduino Forum
```
**Blink every 1s:**The module is running but hasn’t made connection to the cellular network yet.
**Blink every 2s:**The GPRS data connection you requested is active.
**Blink every 3s:**The module has made contact with the cellular network & can send/receive voice and SMS.
```

### Vendors

#### I first tried with Hologram.io.

I tried first by putting  the sim800L upto near my  window using USB power to the pico and 5V wall power for the simb00l.

I connected a few times. But only about 3 or 4 in a short window of time. Out of probably a 100 attempts over a few days.


I tried on the roof: 

![image](https://github.com/user-attachments/assets/05b6f8c8-2fc3-440b-99e0-176c2ab6f1c9)


I tried being mobile in an open area:

![image](https://github.com/user-attachments/assets/cc82cffb-90fe-4cbd-bbed-6da64a1ee2ee)


Really never got a consistent connect after the first few times.


Support told me it's a dice roll for now:

![image](https://github.com/user-attachments/assets/ad40d289-8f49-4145-a4d8-88a86f9c9e24)

NOTE: There is very little in terms of how to *actually get online* with a microcontroller using a consistent step by step process. 

It's mostly anecdotes here and there that you cobble together (voila!).



## Full Micropython Example

```
import time
from gsmuart import uart

def get(sleep=2):
    time.sleep(sleep);
    try:
        r=uart.read()
        print(r.decode())
    except AttributeError as e:
        if 'NoneType'  in str(e):
            print(f"No Real data - got {r}")
    except UnicodeError as e:
        print(f"No Good data - got {r}")
        
""" Basic Diagnostics First """    

uart.write(b'AT\r\n')                 ; get()
uart.write(b'ATE 0\r\n')              ; get()
uart.write(b'ATI\r\n')                ; get()
uart.write(b'ATE1V1\r\n')             ; get()
uart.write(b'AT+CGMM\r\n')            ; get()
uart.write(b'AT+CCID\r\n')            ; get()
uart.write(b'AT+cfun=1\r\n')          ; get()
uart.write(b'AT+CSTT="hologram"\r\n') ; get()
uart.write(b'AT+CPIN?\r\n')           ; get()
uart.write(b'AT+CGDCONT?\r\n')        ; get()

#AT+CSQ Signal quality report
uart.write(b'AT+CSQ\r\n')             ; get()

#AT+CIPSTATUS Query current connection status
uart.write(b'AT+CIPSTATUS\r\n')       ; get()
uart.write(b'AT+CGATT?\r\n')          ; get()

#AT+CIICR Bring up wireless connection with GPRS or CSD
uart.write(b'AT+CIICR\r\n')           ; get(15)

#AT+CIFSR Get local IP address
uart.write(b'AT+CIFSR\r\n')           ; get()

#AT+CGREG Network registration status
uart.write(b'AT+CGREG\r\n')          ; get()

#Checks which network you are connected to.
uart.write(b'AT+COPS?\r\n')       ; get()
#I.E +COPS: 0,0,"T-Mobile USA"

#Check the time - just to see what happens
uart.write(b'AT+CCLK?\r\n')          ; get()

""" If all that is successful ... """
uart.write(b"AT+CMEE=1\r\n"); get() 
uart.write(b"AT+CGATT=1\r\n"); get()
uart.write(b"AT+CGPADDR=1\r\n"); get() 

uart.write(b"AT+HTTPINIT\r\n")                ; get()
uart.write(b"AT+HTTPPARA=\"CID\",1\r\n")      ; get()
uart.write(b"AT+HTTPPARA=\"URL\",\"http://www.google.com:80/\"\r\n") ; get()
uart.write(b"AT+HTTPACTION=0\r\n")            ; get()
uart.write(b"AT+HTTPREAD\r\n")                ; get()
uart.write(b"AT+HTTPTERM\r\n")                ; get()
uart.write(b"AT+CIPSHUT\r\n")                 ; get()

""" In case it does not connect in a timely manner """
while True:
    uart.write(b'AT+CIPSTATUS\r\n') ; get()
    time.sleep(1)
    uart.write(b'AT+CIFSR\r\n')     ; get()
    time.sleep(1)
    uart.write(b'AT+CGREG\r\n')     ; get()
    time.sleep(1)
    uart.write(b'AT+CSQ\r\n')             ; get()
    time.sleep(1)
    time.localtime()
```

### Connected 

I connected a few times. I live in NYC , in a lively connected city, so I figured connectivity would be fine... 

This was pretty cool. I actually connected:

```
>>> uart.write(b"AT+CNETSCAN\r\n"); time.sleep(5); print(uart.read())
13
b'\r\nOperator:"T-Mobile USA",MCC:310,MNC:260,Rxlev:53,Cellid:CF00,Arfcn:1709\r\n\r\nOK\r\n'

>>> uart.write(b"AT+CENG=2\r\n"); time.sleep(5); print(uart.read())
11
b'AT+CENG=2\r\r\nOK\r\n\r\n+CENG: 0,"0685,57,00,310,260,16,cf00,04,00,7d73,255"
                       \r\n+CENG: 1,"1585,34,27,310,260,7d73"
                       \r\n+CENG: 2,"1636,28,13,310,260,7d73"
                       \r\n+CENG: 3,"1637,20,49,310,260,7d73"
                       \r\n+CENG: 4,"1634,16,11,310,260,7d73"
                       \r\n+CENG: 5,"1662,41,00,,,0000"  /\----- seems to be the 'lac'
                       \r\n+CENG: 6,"1663,41,00,,,0000"
                       \r\n'
```


Given the diagnostic info, I was able to find my myself on a map after following the GPS reference and converting:

```
>>> int(0xCF00)
52992

>>> int(0xCF01)
52993

>>> int(0x7d73)
32115

```

![image](https://github.com/user-attachments/assets/56e861a8-1098-4bfc-b527-65b7464581ad)


So that was pretty cool.


## Takeaways/ Learnings
- Keep your costs low and test out vendors before commiting. They tend to believe "Everything is Awesome".


## References

## SIM800L Resources

| Topic | Link | Topic | Link |
|---|---|---|---|
| SIM800L Network Registration Issue Solved | [Arduino Forum](https://forum.arduino.cc/t/sim800l-not-registering-to-network-issue-solved/593251) |Getting GPS w/Cell data|[www.re-innovation](https://www.re-innovation.co.uk/docs/find-location-with-sim800l/)  |
| Registering using a Pi Pico and a SIM800L | [Hologram Forum](https://community.hologram.io/t/registering-with-hologram-using-a-pi-pico-and-a-sim800l/4986/4) |Getting Started with SIM800L | [Hologram Forum](https://community.hologram.io/t/getting-started-with-hologram-and-sim800l/4417/4) |
| Discussion on SIM800L (Thread 1) | [Reddit Thread 1](https://www.reddit.com/r/IOT/comments/1e344zy/comment/ld7c2om/?context=3) | Discussion on SIM800L (Thread 2) | [Reddit Thread 2](https://www.reddit.com/r/embedded/comments/1e0zs95/comment/lct313d/) |
| Hologram AT Command Workshop | [Hologram WorkShop](https://github.com/HologramEducation/AT-Workshop) | AT  Reference Manuals | [AT Commands](https://sixfab.com/wp-content/uploads/2021/02/Telit_IP_Easy_User_Guide_r24.pdf)  and [TCPIP Note, section 8](https://cdn-shop.adafruit.com/product-files/1946/SIM800+Series_TCPIP_Application+Note_V1.01.pdf)|
| What Boards are good | [MicroPython Forum](https://forum.micropython.org/viewtopic.php?t=5270) | PDP DEACT - Stack Overflow | [SO](https://stackoverflow.com/questions/62138595/sim800l-atciicr-always-goes-to-pdp-deact-state) |


## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.


