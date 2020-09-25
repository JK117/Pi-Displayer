import socket
import json
from urllib.request import urlopen


def get_hostname():
    return socket.gethostname()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('1.1.1.1', 80))
    ip = s.getsockname()[0]
    return ip


def get_public_ip(url='https://ipinfo.io/json?token=592622f207ab66'):
    ip = json.load(urlopen(url))['ip']
    return ip


# def fetch_data(url):
#     req = Request(url)  # 请求url（GET请求）
#     with urlopen(req) as f:     # 打开url请求（如同打开本地文件一样）
#         return json.loads(f.read().decode('utf-8'))  # 读数据 并编码同时利用json.loads将json格式数据转换为python对象
#
#
# URL = 'http://ipinfo.io/?token=592622f207ab66'
# data = fetch_data(URL)
# print(data)


if __name__ == "__main__":
    try:
        hostname = get_hostname()
        local_ip = get_local_ip()
        public_ip = get_public_ip()
    except IOError:
        print("Error: unable to get ips")
    else:
        print("Hostname: " + hostname)
        print("Local IP: " + local_ip)
        print("Public IP: " + public_ip)