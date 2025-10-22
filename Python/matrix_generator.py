import time
import random

column = int(input("Matris sütun sayısı girin: "))
row = int(input("Matris satır sayısını girin: "))

for i in range(0,row):
    output = []
    for j in range(0,column):
        m1 = random.randint(0,10)
        output.append(m1)
    time.sleep(0.1)
    print(' '.join(str(x) for x in output))