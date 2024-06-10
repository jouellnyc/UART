## ESP01s Flashing

## Prerequisites

- ESP01s

[These](https://www.amazon.com/dp/B08QF24GZZ) came in a pack of 5.
 
### Inital Failures

Lots of garbage characters:

![image](https://github.com/jouellnyc/UART/assets/32470508/8d172a3e-04fd-49a7-a6f0-33c12037bdcd)

I took the defaults trying to flash the esp01s's.

## References 
- [Reddit](https://www.reddit.com/r/esp32/comments/1dbk6d9/comment/l7s0gjd/?context=3)
- [Espressif flash modes](https://docs.espressif.com/projects/esptool/en/latest/esp8266/esptool/flash-modes.html)
- [MP Forum 1](https://github.com/micropython/micropython/issues/11656)
- [MP Forum 2](https://github.com/thonny/thonny/issues/2801)

## Takeaways / Learnings
- Use the settings in MP Forum 1:
- ![image](https://github.com/jouellnyc/UART/assets/32470508/69c24751-969b-4743-935f-77e9f7e6d20c)
- esp01s's are out of date, but still fun for hobbies. No reason not to get the 4MB version.
- esp01's are not capable of ppp. They don't have enough ram:
![image](https://github.com/jouellnyc/UART/assets/32470508/7ebbb731-9511-4462-98d1-fb43423f37bf)

  

