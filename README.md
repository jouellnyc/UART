# UART projects
This repository provides an examples of how to use UART with microcontrollers in various configurations.

Here's a nice short video on UART (not mine, image below is the author's as well) to get started if unfamiliar with UART:

https://www.youtube.com/watch?app=desktop&v=JuvWbRhhpdI

![image](https://github.com/jouellnyc/UART/assets/32470508/64903885-f112-42c4-98f4-de987f2aeeee)

Here are the projects:

## 1. [ESP32 to ESP32 - UART - Simple Example](esp32_simple/)
- It was quite the effort to get 2 esp32 devices with SPIRAM to speak to each other over a simple UART.
- It seemed like the information was hidden, but it was just not obvious.

## 2. [ESP32 to ESP32 - UART - RS-422 Example](esp32_rs422/)
- Oddly enough, it was quite the effort to get 2 esp32 devices to speak to each other over rs-422 modules.
- Yet again, it seemed like the information was hidden, but it was just not obvious.

## 3. [ESP32 to ESP32 - UART - RS-485 Example](esp32_rs485/)
- It was easy to get 2 esp32 devices to speak to each other over rs-485 modules, but full duplex was quite tricky.
- We simulate that and try to create a 'uart ping' to see how quickly the data comes 'back'.

## 4. [ESP32 to ESP32 - UART - RS-232 Example](esp32_rs232/)
- RS-232 poised a few challenges, but we overcame them.

## 5. [Raspberry Pi Zero to Pi Zero - UART Simple Example with PPP ](pizero_simple/)
- This project can be a physical connection proxy for WPA2-Enterprise deployments
- This is a full OS and more details are needed than just a simple script to properly deploy.

## 6. [Raspberry Pi Zero to ESP32 - UART Simple Example - with PPP ](esp32_pizero/)
- This project can also be a physical connection proxy for WPA2-Enterprise deployments using jumpers and PPP.
- This is a full OS as server and microcontroller as client.

## 7. [Pi Zero to ESP32 to ESP32 - Multi UART Simple Example - with PPP ](esp32_pizero_esp32_ppp_uart/)
- This project uses multiple UARTS at once with an ESP32 in the middle. Building heavily on other projects.

## 8. [ESP01S to ESP32 - Simple Example ](esp01s_esp32/)
- ESP01s connecting to an ESP32! Includes how to flash the olders models. (Also an UART 'Easter Egg').


Overall Notes:

- Finding the right pin mapping for each esp32 can be a little tricky with so may boards and manufacturers. 

- These projects follow https://doc.riot-os.org/group__boards__esp32s3__devkit.html

![image](https://github.com/jouellnyc/UART/assets/32470508/cdc2d37a-1bed-4a70-a8e8-bac5a0165541)

Source - https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html


