
try:
    n=int(input("Enter a number "))
    i=2
    flag=True
    while(i<=int(n**(1/2))):
        if n%i==0:
            flag=False
            break
    i+=1;
except ValueError:
    print("Error. Please enter numeric input .")


if flag==True:
    print(str(n) + " is a Prime number.")
else:
    print(str(n)+ " is not a Prime number.")