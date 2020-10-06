from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
import time
import status


def main():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, fill="black", outline="white")
        draw.text((10, 10), "Raspberry Pi", fill="white")
        draw.text((10, 30), "Start Up Completed", fill="white")
    time.sleep(10)
    for i in range(5):
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="white")
        time.sleep(10)

    # while True:
    #     cpu_temp = status.get_cpu_temp()
    #     cpu_usage = status.get_cpu_usage()
    #     # ram_info = status.get_ram_info()
    #     # disk_usage = status.get_disk_info()
    #     with canvas(device) as draw:
    #         draw.rectangle(device.bounding_box, fill="black", outline="white")
    #         draw.text((10, 5), "CPU Temperature: ", fill="white")
    #         draw.text((10, 15), cpu_temp + "'C", fill="white")
    #         draw.text((10, 25), "CPU Usage: ", fill="white")
    #         draw.text((10, 35), cpu_usage + "%", fill="white")
    #     time.sleep(1)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        device = sh1106(serial)
        main()
    except KeyboardInterrupt:
        pass
