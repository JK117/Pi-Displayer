from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
import time

# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
# serial = i2c(port=1, address=0x3C)
serial = spi(device=0, port=0, cs_high=True)

# substitute with ssd1306, ssd1325, ssd1331, sh1106
device = sh1106(serial)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, fill="black", outline="white")
    draw.text((10, 10), "Raspberry Pi", fill="white")
    draw.text((10, 30), "Start Up Completed", fill="white")
time.sleep(15)