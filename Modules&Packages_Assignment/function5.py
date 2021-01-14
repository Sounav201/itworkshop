
def factorial(n):
    res =1
    for i in range(1 , n +1):
        res*=i

    return res


def f5(n,r):
    if n==0 or r==0:
        return 1
    res= int((factorial(n)/(factorial(n-r)*factorial(r) )))
    return res
