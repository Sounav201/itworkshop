#Write pay program using try and except so that your program handles
#non-numeric input gracefully by printing a message and exiting the program.


while True:

    try:
        a = int(input("Enter a number "))
        a=int(a)
        break
    except ValueError:
        print("Error, please enter numeric input ")

