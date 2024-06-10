## ESP01s Flashing

## Prerequisites

- ESP01s

[These](https://www.amazon.com/dp/B08QF24GZZ) came in a pack of 5.
 
### Inital Failures

## References 
- [https://esp32io.com/tutorials/esp32-rs422](https://electronics.stackexchange.com/questions/714994/why-does-rs-232-communication-fail-between-these-3-esp32s)
- https://forum.arduino.cc/t/why-does-rs-232-communication-fail-between-these-3-esp32s/1266309

## Takeaways / Learnings
- Firstly, to send with RS-232 like this, you need a null modem cable. I thought I had one, but it was a straight through cable.
- Using an IDE/console via USB will use UART0, you'll need to use UART1 or UART2 as described to see any output/test/program.
- There was confusion on how these work in terms of needed connection and how to connect them in the forums. I was subsequently able to connect these without the esp32 sharing a ground with the rs-232 to TTL module at all:
