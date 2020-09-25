import os
import time


# Return CPU temperature as a character string
def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


# def get_cpu_temp():
#     return os.popen('/opt/vc/bin/vcgencmd measure_temp').read()[5:9]


# def get_cpu_temp():
#     with open("/sys/class/thermal/thermal_zone0/temp") as tempFile:
#         res = tempFile.read()
#         res = str(float(res)/1000)
#     return res


# Return % of CPU used by user as a character string
def get_cpu_usage():
    return str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())


# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def get_ram_info():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:4]


# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def get_disk_usage():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:5]


def get_status():
    # CPU information
    cpu_temp = get_cpu_temp()
    cpu_usage = get_cpu_usage()

    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    ram_stats = get_ram_info()
    ram_total = round(int(ram_stats[0]) / 1000, 1)
    ram_used = round(int(ram_stats[1]) / 1000, 1)
    ram_free = round(int(ram_stats[2]) / 1000, 1)

    # Disk information
    disk_stats = get_disk_usage()
    disk_total = disk_stats[0]
    disk_used = disk_stats[1]
    disk_scale = disk_stats[3]

    output_str = 'SYSTEM STATUS\n' \
                 'CPU Temperature: {}\nCPU Usage: {}\n\n' \
                 'RAM Total: {}\nRAM Used: {}\nRAM Free: {}\n\n' \
                 'DISK Total Space: {}\nDISK Used Space: {}\nDISK Used Percentage: {}\n\n'.format(cpu_temp, cpu_usage, ram_total, ram_used, ram_free, disk_total, disk_used, disk_scale)
    # print('CPU Temperature: ' + cpu_temp)
    # print('CPU Usage: ' + cpu_usage)
    # print('')
    # print('RAM Total: ' + str(ram_total) + ' MB')
    # print('RAM Used: ' + str(ram_used) + ' MB')
    # print('RAM Free: ' + str(ram_free) + ' MB')
    # print('')
    # print('DISK Total Space: ' + str(disk_total) + 'B')
    # print('DISK Used Space: ' + str(disk_used) + 'B')
    # print('DISK Used Percentage: ' + str(disk_scale))
    return output_str


if __name__ == '__main__':
    for i in range(10):
        time.sleep(1)
        print(get_status(), end='\r')
