
def rainbow_generator(step_size=5):

    red_value, green_value, blue_value = 255, 0, 0  # Start with red

    while True:
        # Red to Yellow
        while green_value < 255:
            green_value = min(green_value + step_size, 255)
            yield red_value
            yield green_value
            yield blue_value

        # Yellow to Green
        while red_value > 0:
            red_value = max(red_value - step_size, 0)
            yield red_value
            yield green_value
            yield blue_value

        # Green to Cyan
        while blue_value < 255:
            blue_value = min(blue_value + step_size, 255)
            yield red_value
            yield green_value
            yield blue_value

        # Cyan to Blue
        while green_value > 0:
            green_value = max(green_value - step_size, 0)
            yield red_value
            yield green_value
            yield blue_value

        # Blue to Magenta
        while red_value < 255:
            red_value = min(red_value + step_size, 255)
            yield red_value
            yield green_value
            yield blue_value

        # Magenta to Red
        while blue_value > 0:
            blue_value = max(blue_value - step_size, 0)
            yield red_value
            yield green_value
            yield blue_value
