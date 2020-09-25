import os


def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp") as tempFile:
        res = tempFile.read()
        res = str(float(res)/1000)
    return res


if __name__ == '__main__':
    print('CPU Temperature = ' + get_cpu_temperature())
