from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import time


def main():
    font_list = [
        # "DejaVuSerif-Bold.ttf",
        "DejaVuSansMono.ttf",
        # "PibotoCondensed-Bold.ttf",
        # "LiberationMono-Bold.ttf",
        "DejaVuSans.ttf",
        # "LiberationSans-BoldItalic.ttf",
        # "Quicksand-Light.ttf",
        # "PibotoLtItalic.ttf",
        "LiberationSans-Bold.ttf",
        # "LiberationMono-Italic.ttf",
        # "PibotoCondensed-BoldItalic.ttf",
        "LiberationMono-Regular.ttf",
        # "LiberationMono-BoldItalic.ttf",
        # "LiberationSerif-BoldItalic.ttf",
        # "LiberationSerif-Italic.ttf",
        "DejaVuSans-Bold.ttf",
        # "PibotoLtBold.ttf",
        # "Piboto-ThinItalic.ttf",
        # "LiberationSans-Regular.ttf",
        # "Piboto-Italic.ttf",
        "Piboto-Regular.ttf",
        # "DroidSansFallbackFull.ttf",
        # "LiberationSans-Italic.ttf",
        # "PibotoLt-Regular.ttf",
        # "Quicksand-Bold.ttf",
        "DejaVuSansMono-Bold.ttf",
        # "LiberationSerif-Regular.ttf",
        # "Piboto-LightItalic.ttf",
        "Piboto-Light.ttf",
        # "PibotoLtBoldItalic.ttf",
        # "Quicksand-Regular.ttf",
        # "PibotoCondensed-Regular.ttf",
        # "Piboto-BoldItalic.ttf",
        # "Quicksand-Medium.ttf",
        # "NotoMono-Regular.ttf",
        # "Piboto-Bold.ttf",
        # "PibotoCondensed-Italic.ttf",
        # "DejaVuSerif.ttf",
        # "Piboto-Thin.ttf",
        # "LiberationSerif-Bold.ttf"
    ]

    pixel_font_list = [
        "tiny.ttf",
        "C&C_Red_Alert_INET.ttf",
        "fontawesome-webfont.ttf",
        "FreePixel.ttf",
        "pixelmix.ttf",
        "Volter__28Goldfish_29.ttf",
        "ProggyTiny.ttf",
        "code2000.ttf",
        "ChiKareGo.ttf",
        "miscfs_.ttf"
    ]

    # for i in range(len(pixel_font_list)):
    #     font = ImageFont.truetype(pixel_font_list[i], 10)
    #     with canvas(device) as draw:
    #         draw.rectangle(device.bounding_box, fill="black", outline="white")
    #         draw.text((10, 10), str(i) + ". This is " + pixel_font_list[i], fill="white", font=font)
    #     time.sleep(2)
    font_0 = ImageFont.truetype(pixel_font_list[0], 10)
    font_1 = ImageFont.truetype(pixel_font_list[1], 10)
    font_2 = ImageFont.truetype(pixel_font_list[2], 10)
    font_3 = ImageFont.truetype(pixel_font_list[3], 10)
    font_4 = ImageFont.truetype(pixel_font_list[4], 10)
    font_5 = ImageFont.truetype(pixel_font_list[5], 10)
    font_6 = ImageFont.truetype(pixel_font_list[6], 10)
    font_7 = ImageFont.truetype(pixel_font_list[7], 10)
    font_8 = ImageFont.truetype(pixel_font_list[8], 10)
    font_9 = ImageFont.truetype(pixel_font_list[9], 10)

    while True:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), pixel_font_list[0], fill="white", font=font_0)
            draw.text((10, 15), pixel_font_list[1], fill="white", font=font_1)
            draw.text((10, 25), pixel_font_list[2], fill="white", font=font_2)
            draw.text((10, 35), pixel_font_list[3], fill="white", font=font_3)
            draw.text((10, 45), pixel_font_list[4], fill="white", font=font_4)
        time.sleep(2)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), pixel_font_list[5], fill="white", font=font_5)
            draw.text((10, 15), pixel_font_list[6], fill="white", font=font_6)
            draw.text((10, 25), pixel_font_list[7], fill="white", font=font_7)
            draw.text((10, 35), pixel_font_list[8], fill="white", font=font_8)
            draw.text((10, 45), pixel_font_list[9], fill="white", font=font_9)
        time.sleep(2)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        device = sh1106(serial)
        main()
    except KeyboardInterrupt:
        pass
