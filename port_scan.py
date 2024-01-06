#import pyfiglet
import sys
import socket
from datetime import datetime
  
#ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
#print(ascii_banner)

target = 'amusoft.uz'
#target = '192.168.21.136'

# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    print('host ',sys.argv[1])
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of Argument")
    print('host ',target)
    target = socket.gethostbyname(target)



start_time = datetime.now()
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(start_time))
print("-" * 50)
exampl_ports = [20,21,22,23,25,53,80,123,135,143,443,3306,3389]
local_open_ports = [135, 445, 5040, 5357, 49604, 49606, 49664, 49665, 49666, 49667, 49668, 49669, 59820]
open_ports = {}

begin_port = 1
end_port = 65536
point_port = 0

try:
     
    # will scan ports between 1 to 65,535
    #for port in exampl_ports:
    for port in range(begin_port,end_port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #socket.setdefaulttimeout(0.001)
            socket.setdefaulttimeout(0.8)
             
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                open_ports[port]=socket.getservbyport(port)
                print("Port {} is open {}".format(port,socket.getservbyport(port)))
            else:
                print("Port {} is not open".format(port))
            point_port = port
            s.close()
        except socket.error:
            open_ports[port]='unknow'
            print("Port {} is open {}".format(port,'unknow'))
            #print("\port : {} Server not responding !!!!".format(port))
             
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()
finally:
    end_time = datetime.now()
    print('Point port ',point_port)
    print('open ports : ',open_ports)
    print("Scanning ended at: " + str(end_time))
    print("Scanning time : ",str(end_time-start_time))
    with open('open_ports.txt', 'w') as f:
        f.write(str(open_ports))


    
#  Test-NetConnection 127.0.0.1 -port 135


