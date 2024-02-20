import socket
import time
import pyfiglet


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

def recurringFX():

    t_host = (str(input("Enter the host to be scanned: ")))   
    t_ip = socket.gethostbyname(t_host)

    print(t_ip)

    start_port = (int(input("Enter the Start Port: ")))
    end_port = (int(input("Enter the End Port: ")))

    for port in range(start_port, end_port+1):
        print("scanning port:",port)    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #need to build socket connection in every port
        sock.settimeout(1)
        result = sock.connect_ex((t_ip, port)) #result is variable which helps to connect with host target ans ex is used when there is no connection with any pthe port then it our for loop will continue
        if result ==0:  #if the connection was successful then it will return 0
            print("port {} is Open \n".format(port))
        else:
           continue
    print("Port Scanning complete \n")
    recurringFX()

recurringFX()






