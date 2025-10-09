import time as t

for i in range(0,7):
    print("System booting...")
    t.sleep(0.3)
    i += 1

t.sleep(1)
while(True):
    a = str(input("Will you be my gf? "))
    if(a.__contains__("yes") or a.__contains__("YES") or a.__contains__("Yes")):
        print("OMG!! I love youu!..")

        break
    else:
        print("not recognized please try again later.")
        continue
    