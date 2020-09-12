#Write a program to prompt the user for principal amount, annual interest, and years. Print total
princ_amt=int(input("Enter the principal amount "))
ann_interest=float(input('Enter the annual interest rate '))
yrs=int(input("Enter the number of years "))
total=princ_amt*(1+(0.01*ann_interest)*yrs)
print("Total future value is ",round(total))

