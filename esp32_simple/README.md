## ESP32 UART Simple Example

##  Prerequisites

| Prerequisite | Details |
|---|---|
| ESP32 board or module | I used 2 x [ESP32-S3-DevKitC-1 (S3-N16R8)](https://www.aliexpress.us/item/3256806014820995.html) from AliExpress |
| MicroPython firmware | I used ["Firmware Support for Octal-SPIRAM"](https://micropython.org/download/ESP32_GENERIC_S3/) and pointed Thonny to the file explicitly. |
| BreadBoard | Pretty much any will do |
| Jumper Wires | Pretty much any will do |

![image](https://github.com/jouellnyc/UART/assets/32470508/a54d2c90-bbec-4d85-8390-7a130d5624d1)

## UART2 Pin Configuration

By default, the ESP32 assigns the following pins to UART2:

| Pin | Description |
|---|---|
| TX | GPIO 17 |
| RX | GPIO 16 |

However, if your ESP32 device has SPI RAM enabled, these pins (GPIO 16 and GPIO 17) are dedicated to the SPI RAM interface and cannot be used for UART2. 
In this case, you need to remap the UART2 signals to different GPIO pins.

### UART2 Pin Remapping (with SPI RAM)

When SPI RAM is enabled, you can remap the UART2 signals to the following pins:

| Pin | Description |
|---|---|
| TX | GPIO 14 |
| RX | GPIO 13 |


Additionally, you can optionally assign the CTS and RTS pins for hardware flow control (I did not):

| Pin | Description |
|---|---|
| CTS | GPIO 8 |
| RTS| GPIO 7 |

For example, you would do this in your MicroPython code:

```python
from machine import UART, Pin

# Without SPI RAM
uart2 = UART(2, baudrate=9600, tx=Pin(17), rx=Pin(16))

# With SPI RAM (remapped pins)
uart2 = UART(2, baudrate=9600, tx=Pin(14), rx=Pin(13))

# Optional: Configure CTS and RTS pins for hardware flow control
# uart2 = UART(2, baudrate=9600, tx=Pin(14), rx=Pin(13), cts=Pin(8), rts=Pin(7))
```

## Physical Connections

| Connection | Details |
|---|---|
| ESP32 UART2 TX | Other Device RX |
| ESP32 UART2 RX | Other Device TX |
| Ground (GND) | Connect both devices' GND pins |

NOTE: Pin 14 may be hard to read. See pics for some visual help. 

<table>
  <tr>
    <th>View 1</th>
    <th>View 2</th>
    <th>Pin 13 and 14</th>
    <th>Creative Cabling</th>
  </tr>
  <tr>
    <td align="center"><img src="pics/esp321.jpg" width="200" height="200"></td>
    <td align="center"><img src="pics/esp322.jpg" width="200" height="200"></td>
    <td align="center"><img src="pics/pin13and14.jpg" width="200" height="200"></td>
    <td align="center"><img src="pics/esp32-bb.jpg" width="200" height="200"></td>
  </tr>
</table>



## Full Micropython Example

In Thonny or other IDE, run/import `send_and_receive.py` on each esp32

With any luck they will both run like this:

<table>
  <tr>
    <th>Thonny</th>
  </tr>
  <tr>
    <td align="center"><img src="pics/thonny_uart.png" width="200" height="200"></td>
  </tr>
</table>

## Takeaways/ Learnings
- As mentioned, the key to success here is remapping the UART for an SPIRAM based esp32.
- A 30 foot cable was able to carry the data uing 9600 or 19200 baud, but 38400 did not work well.


| Cable/Wire | Speed | Baud|length|Pic/Other|
|---|---|---|---|---|
| 2 x [Basic Dupont Jumper](https://www.amazon.com/gp/product/B07GD2BWPY/) connected with terminal connector | 35 ms | 9600 | 20 cm | <img src="pics/2x_b_dpnt.jpg" width="100" height="100">|
| Basic Dupont Jumper | 50 ms | 9600 | 10 cm  | <img src="pics/b_dpnt.jpg" width="100" height="100"> |
| Basic Dupont Jumper + [22 AWG Gauge Tinned Copper Stranded ](https://www.temu.com/goods.html?_bg_fs=1&goods_id=601099513962206&sku_id=17592200180902) + Connector | 35 ms | 9600 | 30 feet | <img src="pics/25_feet.jpg" width="100" height="100"> |
| Basic Dupont Jumper + 30 feet 22 AWG Gauge Tinned Copper Stranded + Connector | 20 ms | 19200 | 30 feet | <img src="pics/25_feet.jpg" width="100" height="100"> |


| Feature | Details |
|---|---|
| Color Options |  
  - Primary: Red  
  - Secondary: Blue  
| Network Connectivity | Requires Wi-Fi connection |

## References

- [Unexpected Make video explains hidden UARTS](https://www.youtube.com/watch?v=3sXtVuMhuoc)
- [ ESP32 Forum post re: UART](https://esp32.com/viewtopic.php?t=30573)
- [ Andreas Spiess UART video ](https://www.youtube.com/watch?v=GwShqW39jlE)
- [Pin out from Espressif](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html)

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

