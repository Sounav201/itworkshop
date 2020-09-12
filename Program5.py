#Write a program in Python to find the root of a quadratic equation taken as input.
import math as m
print("Let the equation be of the form of ax^2+bx+c=0 ")
a=int(input("Enter the value of coefficient of x^2 "))
b=int(input("Enter the value of coefficient of x "))
c=int(input("Enter the value of constant c "))
D=m.sqrt(b**2-4*a*c)
x1=(-b + D)/(2*a)
print("The value of x is ",x1)
