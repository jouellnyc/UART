## ESP01S to ESP32 Example Simple Example

## Prerequisites

- An ESP01s.  [These](https://www.amazon.com/dp/B08QF24GZZ) came in a pack of 5:
- An ESP32 like we've been using.
  
### Upfront
ESP01S take a lot of extra care and patience. First we need to flash, then we address the UART.

## ESP01s Flashing

<img src="https://github.com/jouellnyc/UART/assets/32470508/fc1c23ec-50d5-4ecb-8d3f-a0b0038837d8" alt="ESP01s" style="float: left; width: 300px; height: 200px; margin-right: 10px;">

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
There are 8 pins on the ESP01, but it could be tricky to use them. You could use 4 of them: GPIO0,1,2,and 3.

See [ESP 01 PIN OUT](https://www.theengineeringprojects.com/wp-content/uploads/2019/03/introduction-to-esp-01.jpg) for a nice picture.


## Takeaways / Learnings
- Typically ESP01s is an updated version of the ESP01 and can have up to 4 MB of flash (vs 1 MB or 500 kb of flash)
- ESP01s use a dark/black PCB (not the lighter blue color).
- Use the settings in MP Forum 1 and as above to successfully flash your esp01s:
- ESP01s's are out of date, but still very fun for hobbies. There is really no reason not to get the 4MB version.
- ESP01s's are not capable of ppp (see above).

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


