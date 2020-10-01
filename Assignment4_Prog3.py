for i in range(1,1001):
    sum = 0
    temp = i
    while temp > 0:
        d = temp % 10
        sum += d ** 3
        temp //= 10
    if i==sum:
        print("Armstrong Number : " + str(i))
