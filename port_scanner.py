import pyfiglet
import sys
import socket
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER",font="slant")
print("\n\n+-+-+-+-+-+ \n Made by:\n+-+-+-+-+-+ +-+-+-+-+-+ \n Kutay KOCA\n+-+-+-+-+-+ +-+-+-+-+-+ \n\n")
print(banner)


target = input(str("Target IP: "))

print("_" * 50)
print("Scanning Target:: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:
    for port in range(1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open >> Protocol Service Name: {}".format(port, socket.getservbyport(port,"tcp")))
            s.close()
except KeyboardInterrupt:
    print("\n Existing :(")
    sys.exit()
except socket.error:
    print("\ Host no responding :(")
    sys.exit()