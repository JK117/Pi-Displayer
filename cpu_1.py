import os


# Return CPU temperature as a character string
def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "")


# Return % of CPU used by user as a character string
def get_cpu_use():
    return str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())


if __name__ == '__main__':
    print('CPU Temperature = ' + get_cpu_temperature())
    print(get_cpu_use())
