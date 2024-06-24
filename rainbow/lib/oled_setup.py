import ssd1306
from machine import Pin, SoftI2C
from oled_pins import scl,sda

oled_width = 128
oled_height = 64

#ssd1306
i2c = SoftI2C(scl=scl, sda=sda, freq=400000)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def clear():
    oled.fill(0)
    oled.show()

def stext(*args, **kwargs):
    oled.text(*args, **kwargs)
    oled.show()

def show_rgb_text(rgb_val):
    clear()
    stext(   'R    G    B' , 27, 17)
    stext(str(rgb_val),      25, 37)  
    