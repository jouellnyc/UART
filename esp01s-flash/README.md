## ESP01S to ESP32 Example Simple Example

## Prerequisites

- An ESP01s.  [These](https://www.amazon.com/dp/B08QF24GZZ) came in a pack of 5:
<img src="https://github.com/jouellnyc/UART/assets/32470508/fc1c23ec-50d5-4ecb-8d3f-a0b0038837d8" alt="ESP01s" style="float: left; width: 300px; height: 200px; margin-right: 10px;">

- An ESP32 like we've been using.
  
### Upfront
ESP01S take a lot of extra care and patience. First we need to flash, then we address the UART.

## ESP01s Flashing

The easiest way to do this is with a [Programmer](https://www.amazon.com/gp/product/B08QMMGZLB/) like this:

<img src="https://github.com/jouellnyc/UART/assets/32470508/e877397d-98e7-4b62-88ed-4313a6334b77" alt="Programmer" style="float: left; width: 300px; height: 200px; margin-right: 10px;">

There is a button that will short GPIO0 to ground. That puts the ESP01 into flash mode.  That being the case, there are usb based esp01 'adapters' that look just like the programmer but do not have buttons on the side to connect ground to gpio0. The net effect is you can get a REPL easily, but you cannot flash the esp01 with it. 

That being the case, you could modify it to be able to burn firmware like the 'programmer' would. If you connect GND to GPIO01 with some dupont jumpers on that USB device you can create the same affect:

<img src="https://github.com/jouellnyc/UART/assets/32470508/d5ebed5e-0feb-44ad-bf84-f8e8dd66a159" alt="ESP32" style="float: left; height: 300px; margin-right: 10px;">

In Thonny try to install the firmware:

![image](https://github.com/jouellnyc/UART/assets/32470508/7d365142-67cc-43e1-be88-771c226ee605)

Hold down the button on the programmer and after you click install, let the button go.

The downside is you may have to swap out the crossed jumpers for straight jumpers if you want to acess the REPL post your flashing. 

 
### Initial Failures

Lots of garbage characters:

![image](https://github.com/jouellnyc/UART/assets/32470508/8d172a3e-04fd-49a7-a6f0-33c12037bdcd)

I took the defaults trying to flash the esp01s's. However a [Thonny issue](https://github.com/thonny/thonny/issues/2801) got me thinking. Let try some explicit settings:

![image](https://github.com/jouellnyc/UART/assets/32470508/69c24751-969b-4743-935f-77e9f7e6d20c)

I explicitly set the flash size to `4MB` vs `keep`.

I also set the flash mode to `qio`, which is supposed to the most common as per Expressif. 

Success.

## PPP

ESP01s doesn't have ppp available in the default image:

![image](https://github.com/jouellnyc/UART/assets/32470508/e6dd2986-a7d4-4d1e-8351-2c8fa7e8d298)

It seems like it would be possible however, it take about 13k to instantiate ppp in an esp32:
 
![image](https://github.com/jouellnyc/UART/assets/32470508/7ebbb731-9511-4462-98d1-fb43423f37bf)

and the ESP01s has about 33k available on boot:

![image](https://github.com/jouellnyc/UART/assets/32470508/ab427af5-8c86-4279-8088-adbcd793bec6)

Perhaps this could be compiled in. More to come if required.

## UART
There are 8 pins on the ESP01, but it could be tricky to use them. I was able to use 4 of them: GPIO0,1,2,and 3. (see References for other ideas about either their usage or adding more devices)

See [ESP 01 PIN OUT](https://www.theengineeringprojects.com/wp-content/uploads/2019/03/introduction-to-esp-01.jpg) for a nice picture.

### ESP01 - ESP32 UART Connection

![image](https://github.com/jouellnyc/UART/assets/32470508/1df32214-cdda-460a-b175-9413f6cc1b9c)

|ESP32 UART| ESP01 UART|GND|
|---|---|
|GPIO13 (TX) |GPIO3(RX) |GND|
|GPIO14 (RX) |GPIO1(TX) |GND|

### ESP01 - I2C OLED  Connection
| Board | Pin 1| Pin 2|Pin 3|
|---|---|
| ESP01 | GPIO0| GPIO2|GND|
| OLED | SCL| SDA|GND|

Also you'll need 3.3V power to the OLED and ESP01 and connect them to `VCC`. 

A [CP2102](https://www.amazon.com/HiLetgo-CP2102-Converter-Adapter-Downloader/dp/B00LODGRV8/) worked nicely. 

Not required but very helpful to see the GPIOs easily: A [Break Out Board](https://www.amazon.com/dp/B01G6HK3KW)

<img src="https://github.com/jouellnyc/UART/assets/32470508/ab140964-deca-4f16-820d-36cd1ca3670f" alt="Break Out Board" style="float: left; width: 300px; height: 200px; margin-right: 10px;">

### UART Problem/Solution
Now, the ESP01 has a TX and RX pin. If you try to use those to connect to another device (ESP32/etc) AND use an IDE like Thonny, it's not going to work out well - a conflict will ensue.  

If I were to paraphrase [this patch](https://github.com/micropython/micropython/commit/afd0701bf7a9dcb50c5ab46b0ae88b303fec6ed3):

"When the ESP01/etc boots and the REPL is started (on hard or soft reset) then UART(0) is automatically attached to it.
If you execute `uos.dupterm(None, 1)` then it is not, freeing the UART for your TX/RX comms to the ESP32/etc"

After that you could also use the other GPIOs for connecting for example a small OLED. Your mileage may vary in terms of what exactly could hook up to the device. Previously I failed to get more than 2 pins working in one project/program.

This is a small script communicating with an ESP32 that writes the received data to the OLED:

```
try:

    from machine import Pin,I2C
    import ssd1306
    i2c = I2C(scl=Pin(0), sda=Pin(2), freq=100000) #Init i2c
    lcd=ssd1306.SSD1306_I2C(128,64,i2c) 

    """
       Without this sleep you may hook up the esp01 w/o the ability to connect 
       and use it's UART for the IDE. Then you can't "Ctrl/C" and may need to reflash.
       (Not that that happened to me or anything)
    """
    import time
    time.sleep(5)
    
    import os
    """
    #Attaching
    uart = [blah/etc]
    uos.dupterm(uart, 1)
    #Detaching:
    """
    os.dupterm(None, 1)

    import machine
    tx_pin = 1 
    rx_pin = 3  
    uart = machine.UART(0, baudrate=9600, tx=tx_pin, rx=rx_pin)

    while True:
        uart.write(f"hello from esp01\n".encode())
        time.sleep(1)
        rx_data = uart.readline()
        if rx_data:
            lcd.text(f"{rx_data}..",0,0)
            lcd.show()
            with open('/uart-data.txt','a') as file:
                file.write(rx_data.decode())
        time.sleep(1)

"""
You are going to be running 'headless'.
It's nice to be able to get some logging when problems happen.
"""
except Exception as e:
    with open('errors.log', 'a') as f:
        f.write("Caught exception: {}\n".format(type(e).__name__))
        f.write("Error message: {}\n".format(e))
```

## Takeaways / Learnings
- Typically ESP01s is an updated version of the ESP01 and can have up to 4 MB of flash (vs 1 MB or 500 kb of flash)
- ESP01s use a dark/black PCB (not the lighter blue color).
- Use the settings in MP Forum 1 and as above to successfully flash your esp01s:
- ESP01s's are out of date, but still very fun for hobbies. There is really no reason not to get the 4MB version.
- ESP01s's are not capable of ppp with latest mp firmware (see above).

## References 
- [Reddit](https://www.reddit.com/r/esp32/comments/1dbk6d9/comment/l7s0gjd/?context=3)
- [Espressif flash modes](https://docs.espressif.com/projects/esptool/en/latest/esp8266/esptool/flash-modes.html)
- [MP Forum 1](https://github.com/micropython/micropython/issues/11656)
- [MP Forum 2](https://github.com/thonny/thonny/issues/2801)
- [MP Download Firmware for esp8266](https://micropython.org/download/ESP8266_GENERIC/)
- [Connecting an esp-01 to a Raspberry Pi Pico over any wire - RPi Forum](https://forums.raspberrypi.com/viewtopic.php?t=337898)
- [Oled and Led on an esp01 - MicroPython Forum (Archive)](https://forum.micropython.org/viewtopic.php?f=16&t=12794&p=70337&hilit=modulusmath+esp01#p69536)
- [Using the GPIO0 /GPIO2 for OUTPUT and RX for INPUT - MicroPython Forum (Archive)](https://forum.micropython.org/viewtopic.php?t=4921)
- [Wired communication between two ESP-01's : r/esp8266](https://www.reddit.com/r/esp8266/comments/pmnib9/wired_communication_between_two_esp01s/)
- [Setting uos.dupterm() on boot - MicroPython Forum (Archive)](https://forum.micropython.org/viewtopic.php?t=5468)
- [ESP 01 PIN OUT](https://www.theengineeringprojects.com/wp-content/uploads/2019/03/introduction-to-esp-01.jpg)
- [esp8266: Change UART(0) to attach to REPL via uos.dupterm interface](https://github.com/micropython/micropython/commit/afd0701bf7a9dcb50c5ab46b0ae88b303fec6ed3)

