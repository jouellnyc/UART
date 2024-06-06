## ESP32 to Rapberry Pico and to ESP32  Example
This is similar to the others except now we have an esp32 usuing multiple UARTs.

## Prerequisites

- 2 x esp32
- A Pi Zero W

These are the same we've been using in the previous projects.
 

# Why? 
This is another physically connected alternative and seeing if we can get an esp32 to use multiple UARTS 'at the same time'. 

## Pi Zero Setup
Same as https://github.com/jouellnyc/UART/blob/main/esp32_pizero

## Physical Connections / Pins 
- For each connection, ensure RX is connected to a TX PIN.

- Here we are using:

| ESP32 #2 Pin | Description | UART|
|---|---|---|
| TX | PIN 14 to ESP #1 PIN 13| 2 |
| RX | PIN 13 to ESP #1 PIN 14| 2 |
| TX | PIN  6 to pizero PIN 10 (GPIO 15) | 1 |
| TX | PIN  7 to pizero PIN 8 (GPIO 14) | 1 |

- See https://pinout.xyz/
- Also have a shared ground (there are many Grounds available).

## Pic

| ![image](https://github.com/jouellnyc/UART/assets/32470508/71363b68-4612-4f49-9cc7-f39508263ce3)|![image](https://github.com/jouellnyc/UART/assets/32470508/978d8521-27af-454e-81ca-a63893099c81)|
|---|---|



## Takeaways/ Learnings
- If any connections fail, ensure line speed is the same.
- If any connections fail, ensure a loop back test (RX to TX from the device to 'itself') .
- This was surprisingly easy to do once the available pins were identified on the ESP32 with multiple UARTS in use ("the hub")

## References
NA

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.
