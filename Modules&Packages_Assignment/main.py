import functions

print('Find your information about the following functions ')

while(1):
    print("1.F(x,y)=F(x-y,y)+1, if y ≤ x ") 
    print("2.F(n,r)=F(n-1,r)+F(n-1,r-1)")  
    print("3.F(n)=F(n/2)+1 if n>1")  
    print("4.F(M,N)=1 if M=0, or M ≥N ≥1, and F(M,N)=F(M-1,N)+F(M-1,N-1), otherwise.")
    print("5.B(m,x)=m!/(x!(m-x)!) where m>x,B(0,0)=B(m,0)=1 and B(m,x)=B(m,x-1)*[(m-x+1)/x]")
    print("\n")
    ch=int(input())
    if ch==1:
        x=int(input('Enter the value of x '))
        y=int(input('Enter the value of y '))
        
        res= (functions.function1.f1(x,y))
        print("Ans: ",res)
    elif ch==2:
        x=int(input('Enter the value of x '))
        y=int(input('Enter the value of y '))
        
        res=(functions.function2.f2(x,y))
        print("Ans: " ,res)

    elif ch==3:
        x=int(input('Enter the value of x '))
        
        res=(functions.function3.f3(x))
        print("Ans: ",res)

    elif ch==4:        
        x=int(input('Enter the value of x '))
        y=int(input('Enter the value of y '))
        
        res= functions.function4.f4(x,y)
        print("Ans: " , res)

    elif ch==5:
        x=int(input('Enter the value of x '))
        y=int(input('Enter the value of y '))
        res= (functions.function5.f5(x,y))
        print("Ans : " , res)

    elif ch==6:
        print('Thank you!') 
        break
    else:
        print('Wrong Input!') 


