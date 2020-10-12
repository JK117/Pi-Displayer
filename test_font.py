from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import time


def main():
    font_list = [
        "DejaVuSerif-Bold.ttf",
        "DejaVuSansMono.ttf",
        "PibotoCondensed-Bold.ttf",
        "LiberationMono-Bold.ttf",
        "DejaVuSans.ttf",
        "LiberationSans-BoldItalic.ttf",
        "Quicksand-Light.ttf",
        "PibotoLtItalic.ttf",
        "LiberationSans-Bold.ttf",
        "LiberationMono-Italic.ttf",
        "PibotoCondensed-BoldItalic.ttf",
        "LiberationMono-Regular.ttf",
        "LiberationMono-BoldItalic.ttf",
        "LiberationSerif-BoldItalic.ttf",
        "LiberationSerif-Italic.ttf",
        "DejaVuSans-Bold.ttf",
        "PibotoLtBold.ttf",
        "Piboto-ThinItalic.ttf",
        "LiberationSans-Regular.ttf",
        "Piboto-Italic.ttf",
        "Piboto-Regular.ttf",
        "DroidSansFallbackFull.ttf",
        "LiberationSans-Italic.ttf",
        "PibotoLt-Regular.ttf",
        "Quicksand-Bold.ttf",
        "DejaVuSansMono-Bold.ttf",
        "LiberationSerif-Regular.ttf",
        "Piboto-LightItalic.ttf",
        "Piboto-Light.ttf",
        "PibotoLtBoldItalic.ttf",
        "Quicksand-Regular.ttf",
        "PibotoCondensed-Regular.ttf",
        "Piboto-BoldItalic.ttf",
        "Quicksand-Medium.ttf",
        "NotoMono-Regular.ttf",
        "Piboto-Bold.ttf",
        "PibotoCondensed-Italic.ttf",
        "DejaVuSerif.ttf",
        "Piboto-Thin.ttf",
        "LiberationSerif-Bold.ttf"
    ]

    for font_name in font_list:
        font = ImageFont.truetype(font_name, 8)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 10), "This is DejavuSansMono", fill="white", font=font)
        time.sleep(1)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        device = sh1106(serial)
        main()
    except KeyboardInterrupt:
        pass
