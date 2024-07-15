from usocket import socket
from machine import Pin,SPI
import network
import time

spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin

"""
???
#DHCP

nic.ifconfig('dhcp')
???

# If you use the Dynamic IP(DHCP), you must use the "nic.ifconfig('dhcp')".
    nic.ifconfig('dhcp')
# If you use the Static IP, you must use the  "nic.ifconfig("IP","subnet","Gateway","DNS")".
    #nic.ifconfig(('192.168.100.13','255.255.255.0','192.168.100.1','8.8.8.8'))
    
    
"""
nic.ifconfig(('192.168.0.252', '255.255.255.0', '192.168.0.197', '8.8.8.8'))
print("sleep 1")
time.sleep(1)
nic.active(True)
time.sleep(1)
print(nic.isconnected())
print(nic.regs())
print(nic.ifconfig())
print(nic.active())

