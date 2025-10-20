small  = [1,2,3,4,5]
middle = [6,7,8,9,10]
big = [11,12,13,14,15]


while(True):
    inp = int(input("Makrometreyi girin: "))
    if inp in small:
        print("small")
    elif inp in middle:
        print("middle")
    elif inp in big:
        print("big")
    else:
        print("extra big")

    if inp == None:
        break
    else:
        continue