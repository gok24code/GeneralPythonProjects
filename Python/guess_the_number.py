import time
import random

sec_num = random.randrange(1,100)
timer = 0
guessed_number = 0
while(True):

    if guessed_number != sec_num:
        guessed_number = int(input("Guess the number: "))
        timer+=1
        if timer > 3:
            print("You've been reach the quota. \n")
            break
        else:
            if guessed_number > sec_num:
                offset = guessed_number-sec_num
                print("you are {} units far away. Please try again. \n".format(offset))
            elif guessed_number < sec_num:
                offset = sec_num - guessed_number
                print("you are {} units far away. Please try again. \n".format(offset) )
            continue
    else:
        print("Kazandın. \n")
        break
