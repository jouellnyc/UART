import time
import machine

import uasyncio as asyncio
from microdot import Microdot, Response

from myipaddress import port
from oled_setup import oled, show_rgb_text, clear
from rgb_lib import set_color
from uart_lib import get_tuple_from_uart, send_tuple_using_uart

app = Microdot()
response = Response()
@app.route('/')
async def index(request):
    return f"{rgb_tuple}"

async def run_microdot():
    try:
        app.run(debug=True,port=port)
    except Exception as e:
        print("Microdot error:", e)

async def read_uart():
    global rgb_tuple
    while True:
        rgb_tuple = get_tuple_from_uart("rs232")
        if rgb_tuple:
            if rgb_tuple == (9,9,9):
                print("Clearing")
                clear()
            else:
                print(f"===== Received {rgb_tuple} ======")
                print(f"== Setting Color on Oled ==")
                set_color(*rgb_tuple)
                print(f"== Setting Color on RGB led ==")
                show_rgb_text(rgb_tuple)
                print(f"== sleeping 1 sec ==")
        await asyncio.sleep(1)
        

async def main():
    task1 = asyncio.create_task(run_microdot())
    task2 = asyncio.create_task(read_uart())
    await asyncio.gather(task1, task2)

try:
    print("Starting server...")
    asyncio.run(main())
except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print("Main error:", e)