#Write a program to check whether a number is Armstrong or not.
a=int(input("Enter a number "))
sum=0
temp=a
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10

if a==sum:
    print(str(a) + " is an Armstrong Number ")

else:
    print(str(a) + " is not an Armstrong Number ")
