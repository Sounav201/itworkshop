import math as m
#Save your name and print it.
name="Sounav Saha"
print(name)

#Add 2 numbers.Subtract 2 numbers. Multiply 2 numbers. Divide 2 numbers Input 2 numbers.
a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
d=int(input("Enter a number "))
e=int(input("Enter a number "))
f=int(input("Enter a number "))
g=int(input("Enter a number "))
h=int(input("Enter a number "))
print("Sum = ", a+b)
print("Difference = ", abs(c-d))
print("Product = " ,e*f)
print("Remainder = ",g%h)

#Divide two numbers truncating the fractional part. Input the two numbers.
no1=int(input("Enter a number "))
no2=int(input("Enter a number "))
res=no1/no2
res1=m.trunc(res)
print(res)
print(res1)

#Find a^b . Input the two numbers.
a1=int(input("Enter the base "))
b1=int(input("Enter the exponent"))
print(a1**b1)

#Print the following any strings
aStr="Hello"
print(aStr)

#Write a string and print 0th letter and 5th letter.
str="Uncopyrightable"
print(str[0])
print(str[4])

#Write two words with an escape sequence in between. Now print it.
str1="Hello \"Sounav\" "
print(str1)

#Print string as a raw string.
string=r"This is \Python"
print((string))

#Perform integer conversion.
val="12"
print((int(val)))
#Perform string conversion.
s1val=11
s2val=19
print((str(s1val))+ str(s2val))

#Concatenate two strings without using ‘+’.
string1="Bat"
string2='man'
print("".join([string1,string2]))

#Concatenate two strings using ‘+’.

string3="Visual"
string4="Studio"
print(string3+string4)

#Take input of a floating-point number and an integer. Multiply them. Add three with the result without saving it as a separate variable. Also, round it up to two decimal places without saving it as a separate variable.


val1=float(input("Enter a decimal number "))
val2=int(input("Enter an integer "))
result=(val1*val2) +3
roundup=round(val1*val2)
print(result)
print(roundup)

