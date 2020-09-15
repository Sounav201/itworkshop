#Write a program which takes input of a number and check whether it is positive or negative

a=int(input("Enter a number"))
if a>0:
    print(str(a)+ " is positive ")
elif a<0:
    print(str(a) + " is negative ")

else:
    print("Number entered is 0 ")


