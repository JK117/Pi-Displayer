from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import time


def main():
    font_dejavu_sans_mono = ImageFont.truetype("DejaVuSansMono.ttf", 16)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, fill="black", outline="white")
        draw.text((10, 10), "This is default", fill="white")
        draw.text((10, 30), "This is DejavuSansMono", fill="white", font=font_dejavu_sans_mono)
    time.sleep(10)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        device = sh1106(serial)
        main()
    except KeyboardInterrupt:
        pass