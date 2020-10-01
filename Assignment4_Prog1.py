total=0
try:
    n=int(input("Enter the number upto which you want the sum of "))

    for i in range(1,n+1):
        total+=i
except ValueError:
    print("Error. Please enter numeric input ")

print("Total sum is  "+ str(total))