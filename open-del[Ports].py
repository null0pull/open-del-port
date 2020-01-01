import win32com.shell.shell as shell


class ocp:
    def __init__(self):
        self.banner()
        print('1.Open Ports\n2.Delete Rule-Ports')
        self.ch()


    def banner(self):
        print('Created By : ')
        print('''
            _    _                        _  __        __               _     
           / \  | |__  _ __ ___   ___  __| | \ \      / /_ _  __ _  ___| |__  
          / _ \ | '_ \| '_ ` _ \ / _ \/ _` |  \ \ /\ / / _` |/ _` |/ _ \ '_ \ 
         / ___ \| | | | | | | | |  __/ (_| |   \ V  V / (_| | (_| |  __/ | | |
        /_/   \_\_| |_|_| |_| |_|\___|\__,_|    \_/\_/ \__,_|\__, |\___|_| |_|
                                                             |___/           

        C	O	P	Y	R	I	G	H	T	©	2019
        ''')
        

    def ch(self):
        try:
            ch=int(input('Enter ur Choice : '))
            if ch==1:
                self.op()
            elif ch==2:
                self.dele()
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
