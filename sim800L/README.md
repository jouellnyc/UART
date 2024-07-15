## Raspi Pici and SIM800L 

##  BackStory
My goal was to get a little bit more involved in Internet of Things From a cellular perspective, not spending a ton of money up front. To that end I did some research and it appeared that the SimCom sim800l module would be a perfect fit.  I went ahead and purchased five of these modules from AliExpress, knowing that a few of them weren't going to work. Sure enough three of them did not power up one of them had a bent SIM card holder but two of them did power up.

Upfront lesson: Always by at least two of the items from Ali Express


| Prerequisite | Details |
|---|---|
| Pi Pico |
|Sim800L|

![image](https://github.com/user-attachments/assets/2e2227dc-60cb-489f-9f6b-476d9e145e15)

## UART Pin Configuration

| Module | Pico |
|---|---|
| SIM800L TX | GPIO 01 |
| SIM800L RX | GPIO 00 |
| SIM800L GND | GND|

Prett Straight Forward:

```
import machine
import time
uart = machine.UART(0, baudrate=115200, tx=machine.Pin(0), rx=machine.Pin(1))
```

## Other Pins

| Module | Pico |
|---|---|
| SIM800L VCC | 5V |
| SIM800L GND | GND |


## Full Micropython Example


## Takeaways/ Learnings
-
## References

- [Unexpected Make video explains hidden UARTS](https://www.youtube.com/watch?v=3sXtVuMhuoc)

## License
This project is licensed under the [MIT License](LICENSE).
Feel free to modify the content as needed, such as adding installation instructions, code examples, or any other relevant information for your project.

