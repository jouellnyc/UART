## ESP32 RS-422  Example

## Prerequisites

- Same as https://github.com/jouellnyc/UART/tree/main/esp32_simple
- Also, 2 x RS-422 modulses. I used [these](https://www.amazon.com/gp/product/B0C1C3VHZW/)

## UART2 Pin Configuration

- Each ESP32 will connect TX to TX on the RS-422 modoule
- Each ESP32 will connect RX to RX on the RS-422 modoule


### RS422 Pin Configuration

## Upfront Notes
- I used a 5V wall power brick as a power supply for both RS422 modules.
- I used USB to power the esp32s.

Why? Neither of these esp32 devices seemed to give adequate output power to power the modules.

Such is life with esp32 boards. I intend to retry with esp32's from Espressif themselves versus those used here.


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

3. Configure UART2 in your MicroPython code:
Same as in https://github.com/jouellnyc/UART/tree/main/esp32_simple

4. Full Example 
Same as in https://github.com/jouellnyc/UART/tree/main/esp32_simple


## Notes
- [Reddit Post on the Confusiion](https://www.reddit.com/r/embedded/comments/1cuo52g/comment/l4qclpu/?context=3)

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

