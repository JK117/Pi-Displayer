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
    font_large = ImageFont.truetype("Quicksand-Bold.ttf", 25)
    font_small = ImageFont.truetype("Quicksand-Bold.ttf", 15)

    # font_large = ImageFont.truetype("DejaVuSansMono.ttf", 25)
    # font_small = ImageFont.truetype("DejaVuSansMono.ttf", 15)

    h = device.height
    w = device.width
    w_0, h_0 = font_large.getsize('0')
    w_colon, h_colon = font_large.getsize(':')
    print(w_0)
    print(w_colon)

    # while True:
    for i in range(20):
        dt = datetime.datetime.now()
        dt_time = dt.strftime('%H:%M:%S')
        dt_date = dt.strftime('%Y-%m-%d')
        dt_day = dt.strftime('%a')

        dt_h = dt.strftime('%H')
        dt_m = dt.strftime('%M')
        dt_s = dt.strftime('%S')

        p_h = w / 2 - w_0 * 3 - w_colon
        p_m = w / 2 - w_0
        p_s = w / 2 + w_0 + w_colon
        p_colon_1 = w / 2 - w_0 - w_colon
        p_colon_2 = w / 2 + w_0

        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            # draw.text((5, 5), dt_time, fill="white", font=font_large)
            draw.text((p_h, 5), dt_h, fill="white", font=font_large)
            draw.text((p_m, 5), dt_m, fill="white", font=font_large)
            draw.text((p_s, 5), dt_s, fill="white", font=font_large)
            draw.text((p_colon_1, 5), ':', fill="white", font=font_large)
            draw.text((p_colon_2, 5), ':', fill="white", font=font_large)
            draw.text((5, 40), dt_date + '   ' + dt_day, fill="white", font=font_small)
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
        # print(spi_device.height)
        # print(spi_device.width)
        # print(spi_device.mode)
        # start_up(spi_device)
        display_time(spi_device)
    except KeyboardInterrupt:
        pass

    # while True:


