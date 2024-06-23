from machine import PWM
from rgb_pins_config import red_pwm, green_pwm, blue_pwm

def set_color(r, g, b):
    # Convert 0-255 values to 0-65535 for PWM
    red_pwm.duty_u16(r * 257)
    green_pwm.duty_u16(g * 257)
    blue_pwm.duty_u16(b * 257)
