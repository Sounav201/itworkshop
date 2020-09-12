#Write a program in Python to add, subtract, multiply, and divide two complex numbers.
import cmath as com
def add(a,b):
    print("Sum = " ,(a+b))

def subtract(a,b):
    print("Difference = " ,(abs(b-a)))

def multiply(a,b):
    print ("Product = ",a*b)

def divide(a,b):
    if a>b:
        print ("Quotient = ",a/b)
    else:
        print ("Quotient = ",b/a)

def operation(a,b,operator):
    operator(a,b)



x1 = int(input("Enter the real part for the complex number "))
y1 = int(input("Enter the imaginary part for the complex number "))
x2 = int(input("Enter the real part for the complex number "))
y2 = int(input("Enter the imaginary part for the complex number "))


z1 = complex(x1, y1)
z2=  complex(x2,y2)

operation(z1,z2,add)        #Passing function as an input
operation(z1,z2,subtract)
operation(z1,z2,multiply)
operation(z1,z2,divide)

