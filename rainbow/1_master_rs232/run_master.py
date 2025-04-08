import time
from colors import colors
from rgb_lib import set_color
from oled_setup import oled, show_rgb_text, clear
from uart_lib import get_tuple_from_uart, send_tuple_using_uart
from rb import voice_sensor, setup, get_cmd_id

# Constants
HOLD_LED_TIME = 1
WAIT_FOR_NEW_CMD_TIME = 1
WAIT_DURING_SPEECH_CMDS = 10

# Command IDs
CMD_CYCLE_COLORS = 115
CMD_OFF = 82
CMD_NO_COMMAND = 255
CMD_CLEAR = 45

# Flags
is_cycling_colors = False
pending_cmd = None

# Color mappings (RGB and names)
COLOR_DATA = {
    116: {"rgb": (255, 0, 0), "name": "Red"},
    117: {"rgb": (255, 165, 0), "name": "Orange"},
    118: {"rgb": (255, 255, 0), "name": "Yellow"},
    119: {"rgb": (0, 255, 0), "name": "Green"},
    120: {"rgb": (0, 255, 255), "name": "Cyan"},
    121: {"rgb": (0, 0, 255), "name": "Blue"},
    CMD_OFF: {"rgb": (0, 0, 0), "name": "Off"},
}

# Reverse mapping: color names to command IDs
COLOR_NAMES_TO_IDS = {data["name"]: cmd_id for cmd_id, data in COLOR_DATA.items()}

def setup_system():
    setup(sensor=voice_sensor)
    print("System initialized")

def show_color(rgb_tuple):
    print(f"= Processing RGB: {rgb_tuple}")
    set_color(*rgb_tuple)
    show_rgb_text(rgb_tuple)
    time.sleep(HOLD_LED_TIME)
    send_tuple_using_uart('rs232', rgb_tuple)

def check_voice_command():
    cmd_id = get_cmd_id(sensor=voice_sensor)
    return cmd_id if isinstance(cmd_id, int) and cmd_id != 0 and cmd_id != CMD_NO_COMMAND else None

def handle_color_command(cmd_id):
    color_info = COLOR_DATA[cmd_id]
    show_color(color_info["rgb"])
    print(f'Color chosen: {color_info["name"]}')
    print(f'Sleeping {WAIT_DURING_SPEECH_CMDS} s')
    time.sleep(WAIT_DURING_SPEECH_CMDS)

def handle_command(cmd_id):
    global is_cycling_colors
    if cmd_id == CMD_CYCLE_COLORS or cmd_id == CMD_NO_COMMAND:
        is_cycling_colors = True
        print("Color cycling starting")
    elif cmd_id == CMD_CLEAR:
        clear()
        send_tuple_using_uart('rs232', (9, 9, 9))
        print(f'Sleeping {WAIT_DURING_SPEECH_CMDS} s after clearing')
        time.sleep(WAIT_DURING_SPEECH_CMDS)
    elif cmd_id in COLOR_DATA:
        handle_color_command(cmd_id)
    else:
        print("Unknown command")

def run_color_cycle():
    global is_cycling_colors, pending_cmd
    for rgb_tuple in colors:
        show_color(rgb_tuple)
        if (cmd_id := check_voice_command()):
            print(f"Command {cmd_id} detected, interrupting cycle.")
            is_cycling_colors = False
            pending_cmd = cmd_id
            return
    is_cycling_colors = False
    print("Color cycle complete")
    time.sleep(3)

def main_loop():
    global pending_cmd
    if is_cycling_colors:
        run_color_cycle()
    else:
        if pending_cmd:
            handle_command(pending_cmd)
            pending_cmd = None
        else:
            print("===== Listening for voice commands...")
            if (cmd_id := get_cmd_id(sensor=voice_sensor)):
                handle_command(cmd_id)
            else:
                print(f'Waiting {WAIT_FOR_NEW_CMD_TIME} to listen for next command...')
                time.sleep(WAIT_FOR_NEW_CMD_TIME)

setup_system()
while True:
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Program terminated by user")
        break
    except Exception as e:
        print(f"Error in main loop: {e}")
        time.sleep(WAIT_FOR_NEW_CMD_TIME)
