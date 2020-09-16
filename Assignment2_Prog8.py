#Write pay program using try and except so that your program handles
#non-numeric input gracefully by printing a message and exiting the program.


while True:

    try:
        hours = int(input("Enter a number "))
        hours=int(hours)
        rate = int(input("Enter the rate "))
        rate=int(rate)
        break
    except ValueError:
        print("Error, please enter numeric input ")
        
payment=hours*rate
print("Pay = ",payment)        

