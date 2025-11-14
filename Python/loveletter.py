import time
import os
falsePositive = False

def charWriter(substring):
    
    loveletter = substring
    for char in loveletter:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()  # Add a newline after the loop for clean output


while(True):
    print("Hello, how are u?")
    ans = str(input("status waiting: "))

    if(ans.__contains__("good") or ans.__contains__("fine")):
        charWriter("\nOooohh nice to see you! Im happy about that!")
        falsePositive = False
        break;
    else:
        falsePositive = True
        break;

if(falsePositive):
    
    charWriter("I hope you'll be good see you later babe. Im gonna say this: \nI love you. Bye babe.")
    time.sleep(1)


print("\n[note this application will close in 2 seconds if you close now of course you can. :D]")
time.sleep(2)

