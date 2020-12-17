def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


n=int(input('Enter the range of numbers whose GCD you want to find  '))
lst=[]
for i in range(0,n):
    no=int(input("Enter the number "))
    lst.append(no)

n1=lst[0]
n2=lst[1]
gcd =find_gcd(n1,n2)

for i in range(2,len(lst)):
    gcd=find_gcd(gcd,lst[i])

print(gcd)


