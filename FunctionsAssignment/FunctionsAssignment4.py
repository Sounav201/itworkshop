def add(num1, num2):
    print(num1 + num2)


def multiply(num1, num2):
    print(num1 * num2)


def subtract(num1, num2):
    print(num1 - num2)

def divide(num1,num2):
    if(num1>num2):
        print(num1/num2)
    else:
        print("Dividend is smaller than divisor! Cannot perform division.")

def calculate(num1, num2, operator):             #"""PASSING A FUNCTION AS AN INPUT!!!!"""
    operator(num1,num2)

def exponent(num1,num2):
    print(num1**num2)


while True:
    print('Enter 1. Add  2. Subtract  3. Multiply  4. Divide  5. Exponent ')
    print('Exit')

    ch=input(('Enter the name of the operation you want to perform '))
    ch=ch.lower()


    if ch=='exit':
        break
    elif ch=="add":
        n1=int(input("Enter the first number  "))
        n2=int(input("Enter the second number  "))
        calculate(n1,n2,add)
    elif ch=="subtract":
        n1=int(input("Enter the first number  "))
        n2=int(input("Enter the second number  "))
        calculate(n1,n2,subtract)
    elif ch=="multiply":
        n1=int(input("Enter the first number  "))
        n2=int(input("Enter the second number  "))
        calculate(n1,n2,multiply)
    elif ch=="divide":
        n1=int(input("Enter the first number  "))
        n2=int(input("Enter the second number  "))
        calculate(n1,n2,divide)
    elif ch=="exponent":
        n1=int(input("Enter the first number  "))
        n2=int(input("Enter the second number  "))
        calculate(n1,n2,exponent)






