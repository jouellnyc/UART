## ESP32 RS-232 Example
This is similar the  RS-422 example, except here we add [RS-232](https://en.wikipedia.org/wiki/RS-232) modules.


## Prerequisites

- Same as [simple uart](https://github.com/jouellnyc/UART/tree/main/esp32_simple)
- 2 RS-232 modules. [These](https://www.temu.com/goods.html?_bg_fs=1&goods_id=601099542772145&sku_id=17592327600831&_x_sessn_id=21k411z4l6) were used:

RS232 to TTL Serial Female to TTL Serial Module Brush Board MAX3232 Chip

<img src="https://github.com/jouellnyc/UART/assets/32470508/9ff61f73-2542-426c-bbb5-d68ff70ddc3f" width="300" height="300">

- A [Null Cable Modem](https://www.amazon.com/dp/B000F43X4G)

<img src="https://github.com/jouellnyc/UART/assets/32470508/426196c1-08da-4bce-9e91-5fbc50ef5278" width="300" height="300">
 
###  Upfront Notes on Power

- As with the RS-485 setup, a 5V wall power brick "makes ground and 5V available" on a shared bread board for the RS-232 modules.
- In fact, each module connects to it's own USB 5V power supply (they could share one 5V power supply), but again these ESP32 did not give enough power to power the MAX3232 chip.
- Each esp32 is still itself powered via USB.
- Each module shares ground with attached esp32 only.

## Physical Connections

- Connect each RS-232 to each other via the Null modem adapter:

![image](https://github.com/jouellnyc/UART/assets/32470508/55b289d6-07d1-4612-a918-f569b2e734af)
  
###  RS-232 Pins to Each ESP21

| RS-232 Module | ESP32          |
|------------------------|----------------|
| GND   | GND (shared on bb not directly to ESP32)  |
| VCC   | None|
| RX | GPIO 14 (remapped as RX)|
| TX | GPIO 13 (remapped as TX)|

In words:

- Each esp32 connects it's GND pin to the shared breadboard.
- Each ESP32 TX connects to TX of each module
- Each ESP32 RX connects to RX of each module

###  RS-232 Modules to BreadBoard
| RS-232 Module | BreadBoard|
|------------------------|----------------|
| GND   | GND |
| VCC   | 5V|


### Changes to the Basic UART code

- None
- We still use UART2 and remap as in  [simple uart](https://github.com/jouellnyc/UART/tree/main/esp32_simple)

```
uart = machine.UART(2, baudrate=9600, tx=tx_pin, rx=rx_pin)
```

## Full Example Code

You can run in full duplex mode with no problem:

- Run `import snr` on esp1 and esp2 at the same time to perform full duplex:

![image](https://github.com/jouellnyc/UART/assets/32470508/bea893f1-dbe4-4250-bae1-d22cf286f36a)

![image](https://github.com/jouellnyc/UART/assets/32470508/a82f34fc-4f28-4987-978e-1641419ca460)


## References 
- [https://esp32io.com/tutorials/esp32-rs422](https://electronics.stackexchange.com/questions/714994/why-does-rs-232-communication-fail-between-these-3-esp32s)
- https://forum.arduino.cc/t/why-does-rs-232-communication-fail-between-these-3-esp32s/1266309
- https://esp32.com/viewtopic.php?p=132940#p132940
- https://esp32io.com/tutorials/esp32-rs232

## Takeaways / Learnings
- Firstly, to send with RS-232 like this, you need a null modem cable. I thought I had one, but it was a straight through cable.
- Note again: Using a console via USB will take
- [These RS-232 to USB cables](https://www.temu.com/goods.html?_bg_fs=1&goods_id=601099534302791&sku_id=17592291701402&_x_sessn_id=tbxee81olz&refer_page_name=bgt_order_detail&refer_page_id=10045_1717371335257_u1x9z3oruh&refer_page_sn=10045) never seemed to work :(
<img src="https://github.com/jouellnyc/UART/assets/32470508/ed79f8ab-8ea2-4ce5-8cad-faeff4246a6e" width="300"> 

- [This RS-232 Card]([https://www.amazon.com/gp/product/B07QQHQHK2/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1](https://github.com/jouellnyc/UART/assets/32470508/91c9f491-ffd9-4614-b198-86f97700518e) worked great:
<img src="https://github.com/jouellnyc/UART/assets/32470508/4260a9b3-8079-4cd6-acad-0251496df26e" width="300">

- [This RS-232 Cable](https://www.amazon.com/gp/product/B017C402NQ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) worked great for Linux PC console access and above card.
<img src="https://github.com/jouellnyc/UART/assets/32470508/4b2b6f3f-8593-4dae-b79c-8db2c47fb942" width="300">

- [This RS-232 Cable](https://www.aliexpress.us/item/3256804406490558.html) worked great for Linux PC console access and above card.
<img src="https://github.com/jouellnyc/UART/assets/32470508/0ee191d7-df3b-4e24-b6a0-6e481c377e87" width="300">
  
## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.
