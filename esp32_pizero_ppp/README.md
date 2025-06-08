## ESP32 Rapberry Pico Zero  Example
This is similar to the  [pizero to pizero](https://github.com/jouellnyc/UART/tree/main/pizero_pizero_ppp) example, here we we add an esp32.

## Prerequisites

- An esp32
- A Pi Zero W

These are the same we've been using in the previous projects.
 

# Why? 

This is another physically connected alternative to wifi-based [wpa-ent-mschapv2-bridge](https://github.com/jouellnyc/wpa-ent-mschapv2-bridge), however, now we don't need a full operating system like on the pi zero, we can use a microcontroller, specifically the esp32, because it has the  ppp software available.


| Cautionary Notes | Description                                             |
|-----------------|---------------------------------------------------------|
| 1. | The ppp configs are not hardened - this is just starting out to get you going|

## Pi Zero Setup
- Setup the Pi Zero to [allow Serial Communications](https://learn.adafruit.com/raspberry-pi-zero-creation/enable-uart)
- see [config.txt](config.txt)
- see [cmdline.txt](cmdline.txt)

## Physical Connections / Pins 

- Make sure the TX of the pi zero is connected to the RX of the esp32. 
- Make sure the TX of the esp32  is connected to the RX of the pi. 

- Here we are using:

| ESP32 Pin | Description |
|---|---|
| TX | GPIO 14 |
| RX | GPIO 13 |

These are again remapped because of SPIRAM usage and to remove any pin conflicts for the UART. Modify if needed. 

| ESP32 Pin | Description |
|---|---|
| TX | GPIO 14 |
| RX | GPIO 15 |

These are the default pi zero pins

- See https://pinout.xyz/
- Also have a shared ground.


## Client 

```
import machine
uart = machine.UART(2, baudrate=9600, tx=13, rx=14)

import network
ppp = network.PPP(uart)
ppp.active(True)
ppp.connect()
```

Once connected, the following should reveal True and the IP settings of the esp32:
```
>>> ppp.isconnected()
True
>>> ppp.ifconfig()
('10.0.5.2', '10.0.5.1', '255.255.255.255', '8.8.8.8')
```


## Server

- /etc/rc.local

```
#!/bin/sh -e
echo "Starting pppd..."
stty -F /dev/ttyAMA0 raw
pppd /dev/ttyAMA0 1000000 10.0.5.1:10.0.5.2 proxyarp local noauth debug nodetach dump nocrtscts passive persist maxfail 0 holdoff 1

```


## Pic
The connections are very straight forward. Here's a photo just the same:
![image](https://github.com/jouellnyc/UART/assets/32470508/ef3294ae-32ff-4389-a5f1-02386e8969a1)

## Takeaways/ Learnings
- Make sure both sides have the same line speed (`pppd /dev/ttyAMA0 9600` or whatever baud you choose). It's easy to forget that!
- Everything works without the esp32 needing to call ppp.ifconfig(()) to set anything at all. It picked up the details from the 'server'.
- We needed 'modules-load=dwc2,g_serial' in cmdline.txt for the communication to flow.
- Interesting how the latency of an icmp packet (much slower) compared to bare 'naked UARTS  for [rs-485](https://github.com/jouellnyc/UART/blob/main/esp32_rs485/README.md) but how the ppp link could withstand higher baud rates.

| Connection | Lowest Latency  |
|------------------------|----------------|
| Dupont Wires - 10 cm - 9600 BAUD   | 180 ms |
| Dupont Wires - 10 cm - 19200 BAUD | 90  ms |
| Dupont Wires - 10 cm - 38400 BAUD | 47  ms |
| Dupont Wires - 10 cm - 57600 BAUD | 32   ms |
| Dupont Wires - 10 cm - 115200 BAUD | 16  ms |
| Dupont Wires - 10 cm - 230400 BAUD | 8.3  ms |
| Dupont Wires - 10 cm - 460800 BAUD | 4.4  ms (inconsistent) |
| Dupont Wires - 10 cm - 921600 BAUD | 2.5  ms (inconsistent) |
| Dupont Wires - 10 cm - 1843200 BAUD | speed not supported by pi zero |


## References

[Raspberry Pi Forums Post](https://forums.raspberrypi.com/viewtopic.php?p=2227171)

[Micropython Forum Post](https://github.com/orgs/micropython/discussions/14538)

[TI forum re: Baud](https://e2e.ti.com/support/microcontrollers/msp-low-power-microcontrollers-group/msp430/f/msp-low-power-microcontroller-forum/832781/ccs-msp430fr5994-what-is-the-max-uart-spi-baud-rates-using-only-dco)

[Failure with Actual Connectivity](https://github.com/orgs/micropython/discussions/15881)
 
## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.
