import os
import time


# Return CPU temperature as a character string
def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    cpu_temp = res.replace("temp=", "").replace("'C\n", "")
    return "CPU Temperature: " + cpu_temp + "'C"


# def get_cpu_temp():
#     return os.popen('/opt/vc/bin/vcgencmd measure_temp').read()[5:9]


# def get_cpu_temp():
#     with open("/sys/class/thermal/thermal_zone0/temp") as tempFile:
#         res = tempFile.read()
#         res = str(float(res)/1000)
#     return res


# Return % of CPU used by user as a character string
def get_cpu_usage():
    cpu_usage = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())
    return 'CPU Usage: ' + cpu_usage + '%'


# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def get_ram_info():
    p = os.popen('free')
    counter = 0
    res = []
    while 1:
        counter = counter + 1
        line = p.readline()
        if counter == 2:
            res += line.split()[1:4]
            break
    # Output is in kb, convert it in Mb for readability
    ram_total = round(int(res[0]) / 1000, 1)
    ram_used = round(int(res[1]) / 1000, 1)
    ram_free = round(int(res[2]) / 1000, 1)
    return 'RAM Total: ' + str(ram_total) + ' MB\n' \
           + 'RAM Used: ' + str(ram_used) + ' MB\n' \
           + 'RAM Free: ' + str(ram_free) + ' MB'


# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def get_disk_usage():
    p = os.popen("df -h /")
    counter = 0
    res = []
    while 1:
        counter = counter + 1
        line = p.readline()
        if counter == 2:
            res += line.split()[1:5]
            break

    return 'DISK Total Space: ' + str(res[0]) + 'B\n' \
           + 'DISK Used Space: ' + str(res[1]) + 'B\n' \
           + 'DISK Used Percentage: ' + str(res[3])


# def get_status():
#     # CPU information
#     cpu_temp = get_cpu_temp()
#     cpu_usage = get_cpu_usage()
#
#     # RAM information
#
#     ram_stats = get_ram_info()
#     ram_total = round(int(ram_stats[0]) / 1000, 1)
#     ram_used = round(int(ram_stats[1]) / 1000, 1)
#     ram_free = round(int(ram_stats[2]) / 1000, 1)
#
#     # Disk information
#     disk_stats = get_disk_usage()
#     disk_total = disk_stats[0]
#     disk_used = disk_stats[1]
#     disk_scale = disk_stats[3]
#
#     print('CPU Temperature: ' + cpu_temp)
#     print('CPU Usage: ' + cpu_usage)
#     print('')
#     print('RAM Total: ' + str(ram_total) + ' MB')
#     print('RAM Used: ' + str(ram_used) + ' MB')
#     print('RAM Free: ' + str(ram_free) + ' MB')
#     print('')
#     print('DISK Total Space: ' + str(disk_total) + 'B')
#     print('DISK Used Space: ' + str(disk_used) + 'B')
#     print('DISK Used Percentage: ' + str(disk_scale))


if __name__ == '__main__':
    print("SYSTEM STATUS")
    print(get_cpu_temp())
    print(get_cpu_usage())
    print('\n')
    print(get_ram_info())
    print('\n')
    print(get_disk_usage())
