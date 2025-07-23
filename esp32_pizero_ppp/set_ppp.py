import time
import network
import machine

# Default UART configuration for PPP
DEFAULT_UART_ID = 2
DEFAULT_BAUDRATE = 9600
DEFAULT_TX_PIN = 13
DEFAULT_RX_PIN = 14

# Initialize UART and PPP interface
def init_ppp(uart_id=DEFAULT_UART_ID, baudrate=DEFAULT_BAUDRATE, tx=DEFAULT_TX_PIN, rx=DEFAULT_RX_PIN):
    uart = machine.UART(uart_id, baudrate=baudrate, tx=tx, rx=rx)
    ppp = network.PPP(uart)
    ppp.active(True)
    return ppp

def connect_ppp(ppp, timeout=10):
    print("Connecting PPP...")
    ppp.connect()
    for i in range(timeout):
        if ppp.isconnected():
            print("PPP connected.")
            print(ppp.ifconfig())
            return True
        time.sleep(1)
    print("PPP connection failed.")
    return False

# When run as a standalone script, attempt to connect
if __name__ == "set_ppp":
    ppp = init_ppp()
    connect_ppp(ppp)
    