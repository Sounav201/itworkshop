#Write a program which takes two integers as input. Print whether the two numbers are equal, less than, or greater than the other.
a=int(input("Enter a number "))
b=int(input("Enter a number "))

if a>b:
    print(str(a) + " is  greater than "+ str(b))

elif a<b:
    print(str(a) + ' is less than ' + str(b))

else:
    print(str(a) + ' is equal to ' + str(b));
