import time

from rgb_pins_config import red_pwm, green_pwm, blue_pwm

def set_color(r, g, b):
    # Convert 0-255 values to 0-65535 for PWM
    red_pwm.duty_u16(r * 257)
    green_pwm.duty_u16(g * 257)
    blue_pwm.duty_u16(b * 257)

def next_color(current_color, step):
    r, g, b = current_color
    
    # Red to Yellow
    if r == 255 and g < 255 and b == 0:
        g = min(g + step, 255)
    
    # Yellow to Green
    elif r > 0 and g == 255 and b == 0:
        r = max(r - step, 0)
    
    # Green to Cyan
    elif r == 0 and g == 255 and b < 255:
        b = min(b + step, 255)
    
    # Cyan to Blue
    elif r == 0 and g > 0 and b == 255:
        g = max(g - step, 0)
    
    # Blue to Magenta
    elif r < 255 and g == 0 and b == 255:
        r = min(r + step, 255)
    
    # Magenta to Red
    elif r == 255 and g == 0 and b > 0:
        b = max(b - step, 0)
    
    return (r, g, b)

def rainbow_cycle(step=1, delay=0.05):
    color = (255, 0, 0)  # Start with red
    while True:
        set_color(*color)
        color = next_color(color, step)
        time.sleep(delay)

# Run the rainbow cycle with a step of 5
if __name__ == "__main__":
    print(__name__)
    rainbow_cycle(step=5)