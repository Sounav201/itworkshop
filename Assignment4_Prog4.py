def SOE(n):

    isPrime=[True for i in range(n+1)]
    isPrime[0]=False
    isPrime[1]=False

    for i in range(2,int(n**(1/2))+1,1):
        for j in range(2*i,n+1,i):
            isPrime[j]=False

    for i in range(1,n+1):
        if isPrime[i]==True:

            print(str(i) + '  ' + str(isPrime[i]))



n=1000
SOE(n)

