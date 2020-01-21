''' Program to print the connected wifi connection details.
used commandpromt command : netsh wlan show network, arp -a and ipconfig/all
netsh - only shows wifi client names
arp   - shows network adapter details like mac address.
ipconfig - shows all network ip details

'''

import subprocess
wifi_connected = subprocess.check_output(["netsh", "wlan", "show", "network"])
wifi_connected = wifi_connected.decode("ascii")
print("\n Pl. find the Wifi Network clients connected to our Wifi..",wifi_connected)
wifi_connected = wifi_connected.replace("\r","")
ls = wifi_connected.split("\n")
ls = ls[4:]  # To extract 4th line of client name only
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        print(ls[x])
    x += 1


# to print mac address
macadd = subprocess.check_output(["arp", "-a"])
macadd = macadd.decode("ascii")
print("\nMAC Address of adapters..",macadd)

      
# To print ip deteails
macip = subprocess.check_output(["ipconfig","/all"])
macip = macip.decode("ascii")
print("\nMAC Address of adapters..",macip)

