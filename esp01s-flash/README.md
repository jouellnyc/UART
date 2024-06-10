## ESP01s Flashing

## Prerequisites

- An ESP01s.  [These](https://www.amazon.com/dp/B08QF24GZZ) came in a pack of 5:

![image](https://github.com/jouellnyc/UART/assets/32470508/fc1c23ec-50d5-4ecb-8d3f-a0b0038837d8)

- The ability to put the ESP01 into flash mode.
The easiest way to do this is with a [Programmer](https://www.amazon.com/gp/product/B08QMMGZLB/) like this:

![image](https://github.com/jouellnyc/UART/assets/32470508/e877397d-98e7-4b62-88ed-4313a6334b77)

You would just plug in the ESP01 and hold down the button on the programmer to put it into flash mode. That will short GPIO0 to ground.

Note that there are usb based ESP01 'adapters' that look just like the programmer but do not have buttons on the side to connect ground to GPIO0. 
The net effect is you can get a REPL easily, but you cannot flash the ESP01 with it.

That being the case, you could create your own 'programmer'. If you twist 2 jumpers together like this:

![image](https://github.com/jouellnyc/UART/assets/32470508/d5ebed5e-0feb-44ad-bf84-f8e8dd66a159)

You can then plug GND to GND and GPIO0 to GPIO0 from the adatper to the ESP01 and have the same effect.

The downside is you may have to swap out the crossed jumpers for straight jumpers if you want to acess the REPL post your flashing. 

 
### Initial Failures

Lots of garbage characters:

![image](https://github.com/jouellnyc/UART/assets/32470508/8d172a3e-04fd-49a7-a6f0-33c12037bdcd)

I took the defaults trying to flash the esp01s's.

## References 
- [Reddit](https://www.reddit.com/r/esp32/comments/1dbk6d9/comment/l7s0gjd/?context=3)
- [Espressif flash modes](https://docs.espressif.com/projects/esptool/en/latest/esp8266/esptool/flash-modes.html)
- [MP Forum 1](https://github.com/micropython/micropython/issues/11656)
- [MP Forum 2](https://github.com/thonny/thonny/issues/2801)
- [MP Download Firmware for esp8266](https://micropython.org/download/ESP8266_GENERIC/)

## Takeaways / Learnings
- Use the settings in MP Forum 1:
  
![image](https://github.com/jouellnyc/UART/assets/32470508/69c24751-969b-4743-935f-77e9f7e6d20c)
I explicitly set the flash size to `4MB` vs `keep`.
I also set the flash mode to `qio`, which is supposed to the most common as per Expressif.

- ESP01s's are out of date, but still fun for hobbies. There is really no reason not to get the 4MB version.

- ESP01s's are not capable of ppp. They don't have ppp available in the default image:

![image](https://github.com/jouellnyc/UART/assets/32470508/e6dd2986-a7d4-4d1e-8351-2c8fa7e8d298)

It seems like it would be possible however, it take about 13k to instantiate ppp in an esp32:
 
![image](https://github.com/jouellnyc/UART/assets/32470508/7ebbb731-9511-4462-98d1-fb43423f37bf)

and the ESP01s has about 33k available on boot:

![image](https://github.com/jouellnyc/UART/assets/32470508/ab427af5-8c86-4279-8088-adbcd793bec6)

Perhaps this could be compiled in. More to come if required.
 

