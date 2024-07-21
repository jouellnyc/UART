## Rainbow Chaser UART

![image](https://github.com/user-attachments/assets/9b0a7d3d-c27a-4945-87ca-22bb7c01c19d)

- Working through ROYGBIV, MCU1 sends an RGB tuple to MCU2 and so on down the line via a different signalling protocol/connection:

```
 
  +---------------------+-------------------------+-------------+----------- -+-----------+--------------+---------+
  |  MCU1  |            |    MCU2    |            |     MCU3    |             |   MCU4    |              |  MCU5   |
  |  (TX)  | RS232 -->  |  (RX)(TX)  |  RS485 --> |   (RX)(TX)  |  RS422 -->  | (RX)(TX)  | ETH/RJ45-->  |  (TX)   |
  +---------------+---------------+---------------+-------------+-------------+-----------+--------------+---------+


```

- Each MCU picks up the RGB tuple and sets the color on it's RGB LED
- Each MCU then sets the text of the RGB tuple on it's  OLED
- Each MCU then passes the tuple to the next MCU

  
##  Prerequisites

| Prerequisite |
|---|
| 3 x ESP32 boards |  
| 2 x  Pi Picos |
| 2 x RS-232 modules|
| 2 x RS-422 modules|
| 2 x RS-485 modules|
| 2 x WizNet RJ-45 modules|

All these parts are the same as the previous except the Wiznet Modules:

[These modules](https://www.aliexpress.us/item/3256804674673261.html?spm=a2g0o.order_list.order_list_main.119.7ace18021LkpOf) on Aliexpress are literally the same module as the Wiznet 5500, and work the same way including connections to the pico, just a different form factor:

![image](https://github.com/user-attachments/assets/9b41f1cf-f282-400d-a84e-f4f0d8e41d4f)


## UART2 Pin Configurations
- These are all using the same type of configs as the individual projects.
-The only difference is they are all connected together.

## Full Micropython Examples
See above - The ordering of the MCUs are just like the ascii diagram - You could just it up to however you like however.

## Takeaways/ Learnings
- This was quite the undertaking. Don't try unless you have lots of patience.

## References

| Title | Description | Link |
|---|---|---|
| **Using Micropython to connect Wiznet W5500 Pico Pis over Ethernet** | Official guide from Wiznet on connecting W5500 Pico Pis with Micropython | https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/Ethernet%20Example%20Getting%20Started%20%5BMicropython%5D.md |
| **MicroPython - Python for microcontrollers (Wiznet vendor page)** | Official Micropython download page with Wiznet specific options | https://micropython.org/download/?vendor=Wiznet |
| **MicroPython - Python for microcontrollers (W5500_EVB_PICO download)** | Download page for Micropython for W5500 EVB and Pico specifically | https://micropython.org/download/W5500_EVB_PICO/ |
| **Using Micropython with W5500: An Introduction** | Blog post by Stephan Hennion on introducing Micropython with W5500 | https://sjhennion.github.io/jekyll/update/2023/09/22/w5500-intro.html |


## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

