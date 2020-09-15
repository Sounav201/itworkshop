#Write pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours (Input: hours and rate).

hrs=int(input('Enter the number of hours the employee worked '))
rate=int(input("Enter the hourly rate "))

if hrs<=40:
    pay=round(rate*hrs)

else:
    pay=round(rate*40 + 1.5*rate*(hrs-40))

print("The total payment to be received by the employee is ",pay)