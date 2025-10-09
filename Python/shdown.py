import time as t
import os as sys


def cdown(delay):
    for i in range(0,delay):
        d=delay
        if i <= delay:
            i+=1
            d -= i
            print(d)

        else:
            return
        t.sleep(0.5)

while(True):
    
    answ = str(input("What's up? : "))    
    if answ.__contains__("good"):
        print("have a bad day!")
        cdown(5)
        sys.system("shutdown /s /t 1")
    elif answ.__contains__("bad"):
        print("dont be sad it will be better.")
        cdown(5)
        sys.system("shutdown -l")
    else:
        print("Not recognized please try again..")