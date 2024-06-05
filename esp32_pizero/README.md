## ESP32 Rapberry Pico Zero  Example
This is similar the  [pizero to pizero](https://github.com/jouellnyc/UART/tree/main/pizero_simple) example, here we we add an esp32.

## Prerequisites

- An esp32
- A Pi Zero W

These are the same we've been using in the previous projects.
 

## Physical Connections

# Why? 

This is another physically connected alternative to wifi-based [wpa-ent-mschapv2-bridge](https://github.com/jouellnyc/wpa-ent-mschapv2-bridge), however now we don't need a full operating system like on tge pi zero, we can use a microcontroller, specifically the esp32, because it has the  ppp software available.


| Cautionary Notes | Description                                             |
|-----------------|---------------------------------------------------------|
| 1. | The ppp configs are not hardened - this is just starting out to get you going|



## Client 

## Server

- /etc/rc.local

```
#!/bin/sh -e
echo "Starting pppd..."
stty -F /dev/ttyAMA0 raw
pppd /dev/ttyAMA0 1000000 10.0.5.1:10.0.5.2 proxyarp local noauth debug nodetach dump nocrtscts passive persist maxfail 0 holdoff 1

```


## Pins

- Make sure the TX of the pi zero is connected to the RX of the esp32. 
- Also have a shared ground.
- See https://pinout.xyz/

## Pic

## Takeaways/ Learnings
Make sure both sides have the same line speed (`pppd /dev/ttyAMA0 9600` or whatever baud you choose). It's easy to forget that!

## References

[Raspberry Pi Forums Post](https://forums.raspberrypi.com/viewtopic.php?p=2227171)

[Micropython Forum Post](https://github.com/orgs/micropython/discussions/14538)

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.