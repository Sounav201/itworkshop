#Write a program which takes temperature as input and also input its type (Centigrade or Fahrenheit). Convert it to other format.

temp=float(input("Enter the the temperature "))

scale=input("What is the type of scale of the temperature you entered ? Press C for Centigrade and F for Fahrenheit ")

if scale=='C':
    conversion=float((9 * temp / 5) + 32)
    print('Temperature is ' + str(conversion)+"F " )

elif scale=='F':
    conversion=5 * (temp - 32) / 9
    print('Temperature is ' + str(conversion) + "C ")

else:
    print('Scale entered is wrong input ')

