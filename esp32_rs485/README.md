## ESP32 RS-485  Example
This is similar the Simple UART example and RS-422 example, except here we add [RS-485](https://en.wikipedia.org/wiki/RS-485) modules.


## Prerequisites

- Same as [simple uart](https://github.com/jouellnyc/UART/tree/main/esp32_simple)
- Also, 2 x RS-485 modules. [These](https://www.aliexpress.us/item/3256805229452181.html) were used.

![image](https://github.com/jouellnyc/UART/assets/32470508/23dc6cf1-073f-46af-8612-8aa6f770caf7)

## Physical Connections

###  Upfront Notes on Power

- As with the RS-422 setup, a 5V wall power brick "makes ground and 5V available" on a shared bread board for the RS-485 modules.

![pic](./pics/rs-485.jpg)

###  Ground Pins on ESP32 

Each esp32  connects it's GND pin to the shared breadboard.


###  TTL Pins from ESP32 to RS-422 Module

Each esp32  connects it's RX/TX to the modules RX/TX, respectively:
 
|  ESP32  | RS-422 Module Pin |
|---|---|
| GPIO 13  | TX |
| GPIO 14  | RX |

Note we still use UART2 and remap as in  [simple uart](https://github.com/jouellnyc/UART/tree/main/esp32_simple)


### RS-422 Module Pins 

1. **Power Supply Connections**

    - Connect the VCC pin of each module to the power rail on the shared breadboard.
    - Connect the GND pin of each module to the ground rail on the shared breadboard.

    ```markdown
    | Module 1 | Breadboard | Module 2 |
    |----------|------------|----------|
    | VCC      | VCC Rail   | VCC      |
    | GND      | GND Rail   | GND      |
    ```

2. **Data Line Connections**

    - Connect the **Y** pin of Module 1 to the **B** pin of Module 2.
    - Connect the **Z** pin of Module 1 to the **A** pin of Module 2.
    - Connect the **Y** pin of Module 2 to the **B** pin of Module 1.
    - Connect the **Z** pin of Module 2 to the **A** pin of Module 1.
    - Use jumper wires to make the connections as described above.

    ```
    Breadboard View:

    +-----------------------------------------+
    |  RS422 Module 1        RS422 Module 2   |
    |  [VCC] --+------------- [VCC]           |
    |  [GND] --+------------- [GND]           |
    |  [ Y ] --+------------- [ B ]           |
    |  [ Z ] --+------------- [ A ]           |
    |  [ Y ] --+------------- [ B ]           |
    |  [ Z ] --+------------- [ A ]           |
    +-----------------------------------------+
    ```


4. Full Example 
- Same as [simple uart](https://github.com/jouellnyc/UART/tree/main/esp32_simple)

## References 
Here are more details in terms of the "Why I did it this way":
- [Reddit Post on the RS-422 and Esp32's](https://www.reddit.com/r/embedded/comments/1cuo52g/comment/l4qclpu/?context=3)
- [Very helpful starting material - esp32io.com](https://esp32io.com/tutorials/esp32-rs422)

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

