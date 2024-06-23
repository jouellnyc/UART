from machine import PWM
from rgb_pin_defs import red_pin, green_pin, blue_pin

red_pwm    = PWM(red_pin)
green_pwm  = PWM(green_pin)
blue_pwm   = PWM(blue_pin)

pwm_freq = 1000
red_pwm.freq(pwm_freq)
green_pwm.freq(pwm_freq)
blue_pwm.freq(pwm_freq)