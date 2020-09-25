import os


def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


if __name__ == '__main__':
    print('CPU Temperature = ' + get_cpu_temperature())
