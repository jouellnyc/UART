import time
import machine
import uasyncio as asyncio

from microdot import Microdot
from myipaddress import port

from oled_setup import oled, show_rgb_text
from rgb_lib import set_color
from uart_lib import get_tuple_from_uart, send_tuple_using_uart

async def read_uart():
    global rgb_tuple
    while True:
        rgb_tuple = get_tuple_from_uart("rs232")
        if rgb_tuple:
            print(f"===== Received {rgb_tuple} ======")
            print(f"== Setting Color on Oled ==")
            set_color(*rgb_tuple)
            print(f"== Setting Color on RGB led ==")
            show_rgb_text(rgb_tuple)
            print(f"== sleeping 1 sec ==")
        await asyncio.sleep(1)

app = Microdot()
@app.route('/')
async def index(request):
    return f"{rgb_tuple}"


async def main():
    print("Starting server...")

    try:
        asyncio.create_task(read_uart())
        await app.start_server(port=port)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print(f"MicroDot stopped on port {port}")

asyncio.run(main())

"""
async def main():
    print("Starting server...")
    asyncio.create_task(read_uart())
    await app.start_server(port=port)

print(f"MicroDot Starting on port {port}")
asyncio.run(main())

"""


