## Rainbow Chaser UART

![image](https://github.com/user-attachments/assets/9b0a7d3d-c27a-4945-87ca-22bb7c01c19d)

- Working through ROYGBIV, MCU1 sends an RGB tuple to MCU2, so on down the line via a different signalling protocol/connection:

```
 
  +---------------------+-------------------------+-------------+----------- -+-----------+--------------+---------+
  |  MCU1  |            |    MCU2    |            |     MCU3    |             |   MCU4    |              |  MCU5   |
  |  (TX)  | RS232 -->  |  (RX)(TX)  |  RS485 --> |   (RX)(TX)  |  RS422 -->  | (RX)(TX)  | ETH/RJ45-->  |  (TX)   |
  +---------------+---------------+---------------+-------------+-------------+-----------+--------------+---------+


```

- Each MCU picks up the RGB tuple and sets the color on it's RGB LED
- Each MCU then sets the text of the RGB tuple on it's  OLED

  
##  Prerequisites

| Prerequisite | Details |
|---|---|
| 3 x ESP32 boards |  [ESP32-S3-DevKitC-1 (S3-N16R8)](https://www.aliexpress.us/item/3256806014820995.html) from AliExpress |
| 2 x  Pi Picos | Picos from anywhere|
| 2 x RS-232 modules|
| 2 x RS-422 modules|
| 2 x RS-485 modules|
| 2 x WizNet RJ-45 modules|

## UART2 Pin Configurations
- These are all using the same type of configs as the individual projects.
-The only difference is they are all connected together.

## Full Micropython Examples
TBD

## Takeaways/ Learnings
- This was quite the undertaking. Don't try unless you have lots of patience.

## References
## Resources

| Title | Description | Link |
|---|---|---|
| **Using Micropython to connect Wiznet W5500 Pico Pis over Ethernet** | Official guide from Wiznet on connecting W5500 Pico Pis with Micropython | [https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/Ethernet%20Example%20Getting%20Started%20%5BMicropython%5D.md] |
| **MicroPython - Python for microcontrollers (Wiznet vendor page)** | Official Micropython download page with Wiznet specific options | https://micropython.org/download/?vendor=Wiznet |
| **MicroPython - Python for microcontrollers (W5500_EVB_PICO download)** | Download page for Micropython for W5500 EVB and Pico specifically | https://micropython.org/download/W5500_EVB_PICO/ |
| **Using Micropython with W5500: An Introduction** | Blog post by Stephan Hennion on introducing Micropython with W5500 | https://sjhennion.github.io/jekyll/update/2023/09/22/w5500-intro.html |


## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

