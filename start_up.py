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
        draw.text((10, 15), "Start Up Completed", fill="white")
    time.sleep(5)


def display_time(device):
    quick_sand_bold_large = ImageFont.truetype("Quicksand-Bold.ttf", 30)
    quick_sand_bold_small = ImageFont.truetype("Quicksand-Bold.ttf", 15)
    for i in range(300):
        dt = datetime.datetime.now()
        dt_date = dt.strftime('%Y-%m-%d')
        dt_time = dt.strftime('%H:%M:%S')
        dt_day = dt.strftime('%a')
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), dt_time, fill="white", font=quick_sand_bold_large)
            draw.text((10, 40), dt_date + '  ' + dt_day, fill="white", font=quick_sand_bold_small)
        time.sleep(0.5)


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
        start_up(spi_device)
        display_time(spi_device)
    except KeyboardInterrupt:
        pass

    # while True:


