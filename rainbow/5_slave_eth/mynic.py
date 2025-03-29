import time
import network
from machine import Pin,SPI

from myipaddress import myip

spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
nic.active(True)
nic.ifconfig((myip, '255.255.255.0', '192.168.0.197', '8.8.8.8'))
#nic.ifconfig('dhcp')
time.sleep(2)
print(nic.isconnected())
print(nic.regs())
print(nic.ifconfig())
print(nic.active())

"""
#DHCP
nic.ifconfig('dhcp')

# If you use the Dynamic IP(DHCP), you must use the "nic.ifconfig('dhcp')".
    nic.ifconfig('dhcp')
# If you use the Static IP, you must use the  "nic.ifconfig("IP","subnet","Gateway","DNS")".
    #nic.ifconfig(('192.168.100.13','255.255.255.0','192.168.100.1','8.8.8.8'))
 
"""

