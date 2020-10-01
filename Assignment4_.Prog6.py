x = 'start'
total = 0

n = 1
while x != 'done':
    try:
        x = input("Enter a number or enter done to exit: ")
        total += int(x)
        n += 1
    except:
        print("Error. Please enter numeric input ")

print("Sum = " + str(total))
print("Count = ", n)
print("Average = ", (total / n))