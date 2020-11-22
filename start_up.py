from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106

from PIL import ImageFont

import time
import datetime
import status


def start_up(device):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, fill="black", outline="white")
        draw.text((10, 5), "Raspberry Pi", fill="white")
        draw.text((10, 15), "start Up Completed", fill="white")
    time.sleep(5)


def display_time(device):
    quick_sand_bold_large = ImageFont.truetype("Quicksand-Bold.ttf", 25)
    quick_sand_bold_small = ImageFont.truetype("Quicksand-Bold.ttf", 15)

    dejavu_sans_mono_large = ImageFont.truetype("DejaVuSansMono.ttf", 25)
    dejavu_sans_mono_small = ImageFont.truetype("DejaVuSansMono.ttf", 15)

    h = device.height
    w = device.width
    w_0 = dejavu_sans_mono_large.getsize('0')
    w_colon = dejavu_sans_mono_large.getsize(':')
    print(w_0)
    print(w_colon)

    # while True:
    for i in range(100):
        dt = datetime.datetime.now()
        dt_time = dt.strftime('%H:%M:%S')
        dt_date = dt.strftime('%Y-%m-%d')
        dt_day = dt.strftime('%a')

        dt_h = dt.strftime('%H')
        dt_m = dt.strftime('%M')
        dt_s = dt.strftime('%S')

        print(dt_h)
        print(dt_m)
        print(dt_s)

        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((5, 5), dt_time, fill="white", font=dejavu_sans_mono_large)
            draw.text((5, 40), dt_date + '   ' + dt_day, fill="white", font=dejavu_sans_mono_small)
        time.sleep(0.1)


def status_info(device):
    while True:
        cpu_temp = status.get_cpu_temp()
        cpu_usage = status.get_cpu_usage()
        # ram_info = status.get_ram_info()
        # disk_usage = status.get_disk_info()
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "CPU Temperature: ", fill="white")
            draw.text((10, 15), cpu_temp + "'C", fill="white")
            draw.text((10, 25), "CPU Usage: ", fill="white")
            draw.text((10, 35), cpu_usage + "%", fill="white")
        time.sleep(1)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        spi_device = sh1106(serial)
        # print(spi_device.height)
        # print(spi_device.width)
        # print(spi_device.mode)
        # start_up(spi_device)
        display_time(spi_device)
    except KeyboardInterrupt:
        pass

    # while True:


