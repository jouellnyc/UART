def create_rainbow():
    # Define rainbow colors (50 colors)
    rainbow_colors = []
    for i in range(50):
        r = int(255 * (1 - i / 49))
        g = int(255 * (i / 49))
        b = 0
        rainbow_colors.append((r, g, b))

    for i in range(50):
        r = 0
        g = int(255 * (1 - i / 49))
        b = int(255 * (i / 49))
        rainbow_colors.append((r, g, b))

    for i in range(50):
        r = int(255 * (i / 49))
        g = 0
        b = int(255 * (1 - i / 49))
        rainbow_colors.append((r, g, b))

    return rainbow_colors


