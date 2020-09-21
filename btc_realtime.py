from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
import requests
import time
import datetime


def get_btc_to_usd():
    URL = "https://api.coincap.io/v2/rates/bitcoin"
    response = requests.get(url=URL)
    response_dict = eval(response.text)
    current_usd_rate = float(response_dict['data']['rateUsd'])
    current_timestamp = response_dict['timestamp']

    return current_usd_rate, current_timestamp


def main():
    today_last_time = "Unknown"
    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                now = datetime.datetime.now()
                today_date = now.strftime("%d %b %y")

                margin = 4

                cx = 30
                cy = min(device.height, 64) / 2

                draw.text((2 * (cx + margin), cy - 8), today_date, fill="white")
                draw.text((2 * (cx + margin), cy), today_time, fill="white")

        time.sleep(10)


if __name__ == "__main__":
    try:
        serial = spi(device=0, port=0, cs_high=True)
        device = sh1106(serial)
        main()
    except KeyboardInterrupt:
        pass
