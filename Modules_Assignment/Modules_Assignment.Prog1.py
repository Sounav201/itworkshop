import calendar

def leap(Year):
        
    if(calendar.isleap(Year)):
        print(str(Year) + " is a leap year!")
    else:
        print(str(Year) + " is not a leap year!")





Year=int(input("Enter the Year "))

leap(Year)

for i in range(2000,2022):
    if(calendar.isleap(i)):
        print(i)

