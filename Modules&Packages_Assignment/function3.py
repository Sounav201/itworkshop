def f3(n):
    if(n==1):
        return 0  
    res=f3(n/2)+1
    return res
