## Rainbow Chaser UART

![image](https://github.com/user-attachments/assets/9b0a7d3d-c27a-4945-87ca-22bb7c01c19d)

![video]('/images/rb.mp4')

- Working through ROYGBIV, MCU1 sends an RGB tuple to MCU2, so on down the line via a different signalling protocol/connection:

````
 
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
- [link](https://link)

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

