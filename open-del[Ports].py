import win32com.shell.shell as shell
from Check_Ports import *


class ocp:
    def __init__(self):
        print('Your External IP >> ',ip)
        self.banner()
        print('1.Open Ports\n2.Delete Rule-Ports')
        print('3.Check for open ports')
        self.ch()


    def banner(self):
        print('Created By : ')
        print("NULL 0 PULL")
        

    def ch(self):
        try:
            ch=int(input('Enter ur Choice : '))
            if ch==1:
                self.op()
            elif ch==2:
                self.dele()
            elif ch==3:
                main()
            else:
                print('check ur ch!')
        except ValueError:
            print('Enter correct value for choices')
    def inp(self):
        global name_rule
        name_rule = str(input('Enter name of Rule : '))
        port = str(input('Enter num of port : '))
        self.name_rule = name_rule
        self.port = port
    def op(self):
        self.inp()
        command = '''netsh advfirewall firewall add rule name=%s protocol=TCP localport=%s action=allow dir=IN & netsh advfirewall firewall add rule name=%s protocol=UDP localport=%s action=allow dir=IN'''%(self.name_rule,self.port,self.name_rule,self.port)
        
        try:
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command)
            print('Successfully!')
        except Exception as error:
            print(error)
            
    def dele(self):
        command = 'netsh advfirewall firewall delete rule name=%s'%(str(input('Enter name of Rule : ')))

        try:
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command)
            print('Successfully!')
        except Exception as error:
            print(error) 

if __name__ == '__main__':
    ocp()

while True:
    r = input('Enter x to exit or r for another action : ')
    if r == 'x':
        exit()
    elif r == 'r':
        ocp()
    else:
        print('Kick Out')
