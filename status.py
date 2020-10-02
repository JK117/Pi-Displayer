import os


# Return CPU temperature as a character string
def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    cpu_temp = res.replace("temp=", "").replace("'C\n", "")
    # return "CPU Temperature: " + cpu_temp + "'C"
    return cpu_temp


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
    # return 'CPU Usage: ' + cpu_usage + '%'
    return cpu_usage


# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def get_ram_info():
    p = os.popen('free')
    counter = 0
    ram_list = []
    while 1:
        counter = counter + 1
        line = p.readline()
        if counter == 2:
            ram_list += line.split()[1:4]
            break

    # Outputs are in KB
    # ram_total = str(round(int(ram_list[0]) / 1000, 1))
    # ram_used = str(round(int(ram_list[1]) / 1000, 1))
    # ram_free = str(round(int(ram_list[2]) / 1000, 1))
    # return 'RAM Total: ' + str(ram_total) + ' MB\n' \
    #        + 'RAM Used: ' + str(ram_used) + ' MB\n' \
    #        + 'RAM Free: ' + str(ram_free) + ' MB'
    return ram_list


# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def get_disk_info():
    p = os.popen("df -h /")
    counter = 0
    disk_list = []
    while 1:
        counter = counter + 1
        line = p.readline()
        if counter == 2:
            disk_list += line.split()[1:5]
            break

    # Outputs are in B
    # return 'DISK Total Space: ' + str(disk_list[0]) + 'B\n' \
    #        + 'DISK Used Space: ' + str(disk_list[1]) + 'B\n' \
    #        + 'DISK Used Percentage: ' + str(disk_list[3])
    return disk_list


if __name__ == '__main__':
    print("SYSTEM STATUS")
    print("CPU Temperature: ")
    print(get_cpu_temp() + "'C")

    print("CPU Usage: ")
    print(get_cpu_usage() + "%")

    ram_info = get_ram_info()
    ram_total = str(round(int(ram_info[0]) / 1024, 1))
    ram_used = str(round(int(ram_info[1]) / 1024, 1))
    ram_free = str(round(int(ram_info[2]) / 1024, 1))
    print('RAM Total: ' + ram_total + ' MB')
    print('RAM Used: ' + ram_used + ' MB')
    print('RAM Free: ' + ram_free + ' MB')

    disk_info = get_disk_info()
    disk_total = disk_info[0]
    disk_used = disk_info[1]
    disk_free = disk_info[2]
    disk_ptg = disk_info[3]
    print('Disk Total: ' + disk_total + 'B')
    print('Disk Used: ' + disk_used + 'B')
    print('Disk Free: ' + disk_free + 'B')
    print('Disk Usage: ' + disk_ptg + '%')
