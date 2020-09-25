import os


def get_cpu_temperature():
    return os.popen('/opt/vc/bin/vcgencmd measure_temp').read()[5:9]


if __name__ == '__main__':
    print('CPU Temperature = ' + get_cpu_temperature())
