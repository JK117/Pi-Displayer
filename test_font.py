from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import time

import platform
import json
import pwd
import os
import re


def display_sys_fonts():
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

    div, mod = divmod(len(font_list), 3)
    for i in range(div):
        font_1 = ImageFont.truetype(font_list[i*3], 15)
        font_2 = ImageFont.truetype(font_list[i*3+1], 15)
        font_3 = ImageFont.truetype(font_list[i*3+2], 15)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), str(i*3) + '. ' + font_list[i*3], fill="white", font=font_1)
            draw.text((10, 20), str(i*3+1) + '. ' + font_list[i*3+1], fill="white", font=font_2)
            draw.text((10, 35), str(i*3+2) + '. ' + font_list[i*3+2], fill="white", font=font_3)
        time.sleep(5)

    if mod == 1:
        font_1 = ImageFont.truetype(font_list[-1], 15)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), str(len(font_list) - 1) + '. ' + font_list[-1], fill="white", font=font_1)
        time.sleep(5)

    if mod == 2:
        font_1 = ImageFont.truetype(font_list[-2], 15)
        font_2 = ImageFont.truetype(font_list[-1], 15)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), str(len(font_list) - 2) + '. ' + font_list[-2], fill="white", font=font_1)
            draw.text((10, 20), str(len(font_list) - 1) + '. ' + font_list[-1], fill="white", font=font_2)
        time.sleep(5)


def display_pixel_fonts():
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

    font_0 = ImageFont.truetype(pixel_font_list[0], 15)
    font_1 = ImageFont.truetype(pixel_font_list[1], 15)
    font_2 = ImageFont.truetype(pixel_font_list[2], 15)
    font_3 = ImageFont.truetype(pixel_font_list[3], 15)
    font_4 = ImageFont.truetype(pixel_font_list[4], 15)
    font_5 = ImageFont.truetype(pixel_font_list[5], 15)
    font_6 = ImageFont.truetype(pixel_font_list[6], 15)
    font_7 = ImageFont.truetype(pixel_font_list[7], 15)
    font_8 = ImageFont.truetype(pixel_font_list[8], 15)
    font_9 = ImageFont.truetype(pixel_font_list[9], 15)

    while True:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), pixel_font_list[0], fill="white", font=font_0)
            draw.text((10, 20), pixel_font_list[1], fill="white", font=font_1)
            draw.text((10, 35), pixel_font_list[2], fill="white", font=font_2)
        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), pixel_font_list[3], fill="white", font=font_3)
            draw.text((10, 20), pixel_font_list[4], fill="white", font=font_4)
            draw.text((10, 35), pixel_font_list[5], fill="white", font=font_5)
        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), pixel_font_list[6], fill="white", font=font_6)
            draw.text((10, 20), pixel_font_list[7], fill="white", font=font_7)
            draw.text((10, 35), pixel_font_list[8], fill="white", font=font_8)
        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), pixel_font_list[9], fill="white", font=font_9)
        time.sleep(5)


def display_candidate_fonts():
    free_pixel = ImageFont.truetype("FreePixel.ttf", 15)
    proggy_tiny = ImageFont.truetype("ProggyTiny.ttf", 15)
    code_2000 = ImageFont.truetype("code2000.ttf", 15)

    liberation_mono_regular = ImageFont.truetype("LiberationMono-Regular.ttf", 15)
    liberation_sans_bold = ImageFont.truetype("LiberationSans-Bold.ttf", 15)
    liberation_serif_bold = ImageFont.truetype("LiberationSerif-Bold.ttf", 15)

    dejavu_sans = ImageFont.truetype("DejaVuSans.ttf", 15)
    dejavu_sans_bold = ImageFont.truetype("DejaVuSans-Bold.ttf", 15)
    dejavu_sans_mono = ImageFont.truetype("DejaVuSansMono.ttf", 15)
    dejavu_sans_mono_bold = ImageFont.truetype("DejaVuSansMono-Bold.ttf", 15)

    quick_sand_regular = ImageFont.truetype("Quicksand-Regular.ttf", 15)
    quick_sand_bold = ImageFont.truetype("Quicksand-Bold.ttf", 15)

    piboto_thin = ImageFont.truetype("Piboto-Thin.ttf", 15)
    piboto_bold = ImageFont.truetype("Piboto-Bold.ttf", 15)
    piboto_lt = ImageFont.truetype("Piboto-Light.ttf", 15)
    piboto_lt_regular = ImageFont.truetype("PibotoLt-Regular.ttf", 15)
    piboto_lt_bold = ImageFont.truetype("PibotoLtBold.ttf", 15)

    while True:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "FreePixel", fill="white", font=free_pixel)
            draw.text((10, 20), "ProggyTiny", fill="white", font=proggy_tiny)
            draw.text((10, 35), "code2000", fill="white", font=code_2000)
        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "LiberationMono-Regular", fill="white", font=liberation_mono_regular)
            draw.text((10, 20), "LiberationSans-Bold", fill="white", font=liberation_sans_bold)
            draw.text((10, 35), "LiberationSerif-Bold", fill="white", font=liberation_serif_bold)
        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "DejaVuSans", fill="white", font=dejavu_sans)
            draw.text((10, 20), "DejaVuSans-Bold", fill="white", font=dejavu_sans_bold)
            draw.text((10, 35), "DejaVuSansMono", fill="white", font=dejavu_sans_mono)

        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "DejaVuSansMono-Bold", fill="white", font=dejavu_sans_mono_bold)
            draw.text((10, 20), "Quicksand-Regular", fill="white", font=quick_sand_regular)
            draw.text((10, 35), "Quicksand-Bold", fill="white", font=quick_sand_bold)

        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "Piboto-Thin", fill="white", font=piboto_thin)
            draw.text((10, 20), "Piboto-Bold", fill="white", font=piboto_bold)
            draw.text((10, 35), "Piboto-Light", fill="white", font=piboto_lt)

        time.sleep(5)
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), "PibotoLt-Regular", fill="white", font=piboto_lt_regular)
            draw.text((10, 20), "PibotoLtBold", fill="white", font=piboto_lt_bold)
        time.sleep(5)


def dfs_fonts_dir(path, receiver):
    for item in os.listdir(path):
        if '.uuid' not in item:
            if re.search(r'.ttf', item):
                name = item.split('.')[0]
                receiver[name] = item
            new_path = path + '/' + item
            if os.path.isdir(new_path):
                dfs_fonts_dir(new_path, receiver)


def get_fonts(is_pixel=False):
    sys = platform.system()
    fonts_dir = ''
    fonts = {}
    if sys == 'Darwin':
        fonts_dir = "/Users/" + pwd.getpwuid(os.getuid())[0] + "/Library/Fonts"
    elif sys == 'Linux':
        if is_pixel:
            fonts_dir = "/usr/share/fonts/truetype/pixel"
        else:
            fonts_dir = "/usr/share/fonts/truetype"
    dfs_fonts_dir(fonts_dir, fonts)
    return fonts


def roll(fonts_dict, device_obj, text=''):
    for font_name, font_file in fonts_dict.items():
        font_small = ImageFont.truetype(font_file, 10)
        font_medium = ImageFont.truetype(font_file, 15)
        font_large = ImageFont.truetype(font_file, 20)
        with canvas(device_obj) as draw:
            draw.rectangle(device.bounding_box, fill="black", outline="white")
            draw.text((10, 5), font_name, fill="white", font=font_small)
            draw.text((10, 15), font_name, fill="white", font=font_medium)
            draw.text((10, 30), font_name, fill="white", font=font_large)
        time.sleep(2)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        device = sh1106(serial)
        # fonts = get_fonts()
        # roll(fonts, device)
        # display_sys_fonts()
        display_candidate_fonts()

    except KeyboardInterrupt:
        pass
