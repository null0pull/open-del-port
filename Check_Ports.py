import socket
from datetime import datetime as dt
from time import sleep ,perf_counter
from requests import get


ip = get('https://api.ipify.org').text


def main():
            start = perf_counter() # To Clac A number of Second takes by code

            hostname = socket.gethostname()    

            chp = int(input('Enter 1 for this computer or 2 to add another ip : '))
            if chp == 1:
                ip = get('https://api.ipify.org').text
            elif chp ==2 :
                ip = input('==> ENTER UR IP ADDRESS : ')
            t1 = dt.now()
            print('Scanning Start > %s ~~ Please Wait... '%ip)
            sleep(1)


            try:
                for port in range(1,6553): #can u change 10000 with 6553 (number of main ports)
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.settimeout(0.002) #Waiting Time For Check
                    if s.connect_ex((ip,port)) == 0:
                        try:
                            serv = socket.getservbyport(port)
                        except socket.error :
                            serv = 'Unknown Service'
                        print('Port %s Open Service:%s'%(port,serv))
                        s.close()
            ##############################################################
                    else:
                        try:
                            serv = socket.getservbyport(port)
                        except socket.error :
                            serv = 'Unknown Service'
                        print('Port %s Time-Out Service:%s'%(port,serv))
                        s.close()
            ###############################################################
                    t2 = dt.now()
                    t3 = t2 - t1
                print('Scanning Completed On %s'%t3)
            except Exception as error :
                print(error)


            print('Your Code Take {} Seconds'.format(perf_counter()-start))

