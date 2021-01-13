import random
import math

def Dieroll(number):
    lst= [0]*7

    for i in range(0,number):
        freq=int(random.randint(1,6))
        lst[freq]+=1

    return lst



res=Dieroll(6000)
result= res[1:]

print("The occurences of various die faces are given below ")

for idx, val in enumerate(result):
    print(str(idx+1) + ": "+ str(val))

