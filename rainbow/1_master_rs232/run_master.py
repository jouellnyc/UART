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
CMD_CYCLE_COLORS = 115 # "Color Mode"
CMD_RED = 116
CMD_ORANGE = 117
CMD_YELLOW = 118
CMD_GREEN = 119
CMD_CYAN = 120
CMD_BLUE = 121
CMD_OFF = 82           # "Reset"

# Color mappings
COLOR_MAPPINGS = {
    CMD_RED: (255, 0, 0),
    CMD_ORANGE: (255, 165, 0),
    CMD_YELLOW: (255, 255, 0),
    CMD_GREEN: (0, 255, 0),
    CMD_CYAN: (0, 255, 255),  # Added cyan
    CMD_BLUE: (0, 0, 255),
    CMD_OFF: (0, 0, 0)
}

def setup_system():
    """Initialize the system components."""
    setup(sensor=voice_sensor)
    print("System initialized")

def show_all(rgb_tuple):
    """
    Display and transmit an RGB color value.
    
    Args:
        rgb_tuple: A tuple of (r, g, b) values (0-255)
    """
    try:
        print(f"===== Processing RGB: {rgb_tuple} =====")
        print("Setting RGB LED color...")
        set_color(*rgb_tuple)
        print("Displaying color on OLED...")
        show_rgb_text(rgb_tuple)
        print(f"Holding display for {HOLD_LED_TIME} seconds...")
        time.sleep(HOLD_LED_TIME)
        print("Sending color via UART...")
        send_tuple_using_uart('rs232', rgb_tuple)        
    except Exception as e:
        print(f"Error in show_all: {e}")

def cycle_colors():
    """Cycle through all predefined colors."""
    try:
        print("Starting color cycle sequence")
        for rgb_tuple in colors:
            show_all(rgb_tuple)
    except Exception as e:
        print(f"Error during color cycling: {e}")
    print("Color cycle complete")

def main():
    """Main program loop."""
    setup_system()
    
    """ Turn off the light (will update screen as 0,0,0) """
    """ then Clear Screen """
    while True:
        try:
            
            print('Listening for voice commands...')
            cmd_id = get_cmd_id(sensor=voice_sensor)
            if cmd_id:
                if isinstance(cmd_id, int):
                    if cmd_id == CMD_CYCLE_COLORS:
                        cycle_colors()
                        time.sleep(3)
                    elif cmd_id == 2:
                        pass
                    elif cmd_id == 255:
                        print('No command, cycling colors')
                        cycle_colors()
                    elif cmd_id == 45:
                        """ CLEAR SCREEN """ 
                        clear()
                        send_tuple_using_uart('rs232', (9,9,9))
                        time.sleep(WAIT_DURING_SPEECH_CMDS)
                    else:
                        print(f'Command received: {cmd_id}')
                        rgb_tuple = COLOR_MAPPINGS.get(cmd_id, (0, 0, 0))
                        print(f'Selected color: {rgb_tuple}')
                        show_all(rgb_tuple)
                        time.sleep(WAIT_DURING_SPEECH_CMDS)
                else:
                    print('Invalid command, cycling colors')
                    cycle_colors()
                
            print(f'Waiting {WAIT_FOR_NEW_CMD_TIME} seconds for next command...')
            time.sleep(WAIT_FOR_NEW_CMD_TIME)
            
        except KeyboardInterrupt:
            print("Program terminated by user")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(WAIT_FOR_NEW_CMD_TIME)

if __name__ == "run_master":
    main()