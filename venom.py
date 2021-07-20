#! /usr/bin/env python3
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
    print(w+"\n\n\tMake payloads using "+w+r+"MSFVenom")
    print(w+"\n\n\tSelect the options for which you want to make "+w+r+"payload"+w+" :\n\n")
    print(w+b+"\t1. "+w+"Android\n")
    print(w+b+"\t2. "+w+"Windows\n")
    print(w+b+"\t3. "+w+"Linux\n")
    print(w+b+"\t4. "+w+"Mac\n")
    
    hl=int(input(w+b+"\n\n\t> "))
    if hl == 1 :
      os.system("python3 pld/and.py")
    elif hl == 2:
      os.system("python3 pld/win.py")
    elif hl == 3:
      os.system("python3 pld/lin.py")
    elif hl == 4:
      os.system("python3 pld/mac.py")
    else :
        print(w+"\n\n\t\tThere was an "+r+"error"+w+" while choosing the options !!")
        time.sleep(5)
        os.system("python3 venom.py")
        exit
if __name__ == "__main__":
    try:
        start()
    except EOFError:
        os.system("clear")
        print(r+"\n Exiting ...\n\n")
        time.sleep(2)
        os.system("python3 banner.py")
        print(r+"\n\n[!]"+w+" Thanks for Using this tools\n\n    follow us \033[4mhttps://github.com/Anonymous24x7\033[0m\n\n    ")
        time.sleep(3)
        exit
    except KeyboardInterrupt:
        os.system("clear")
        print(r+"\n Exiting ...\n\n")
        time.sleep(2)
        os.system("python3 banner.py")
        print(r+"\n\n[!]"+w+" Thanks for Using this tools\n\n    follow us \033[4mhttps://github.com/Anonymous24x7\033[0m\n\n    ")
        time.sleep(3)
        exit