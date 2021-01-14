def f4(m,n):
    if(m==0 or ((m>=n) and n>=1)):
        return 1
    else:
        res=f4(m-1,n)+ f4(m-1,n-1)
        return res
