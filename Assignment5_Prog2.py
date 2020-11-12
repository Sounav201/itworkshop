#NAME: SOUNAV SAHA 2nd Year CSE
def NonFib(n):
    current=3     #Add the gap between two consecutive fibonacci numbers. The sum of the gap is the answer.
    prev=2
    before_prev=1

    while n>0:
        before_prev=prev
        prev=current
        current=before_prev+prev   #generating the current fibonacci sequence

        n-=current-prev-1          #n is the number of fibonacci numbers between current and prev

    n+=current-prev-1             # Removing the last added gap and make sure n is positive

    return (n+prev)               # Adding  n to the last fibonacci number


n=int(input("Enter the range of generating Non-fibonacci numbers "))
res=NonFib(n)
print("The number of non-fibonacci numbers are " + str(res))

#x=(input("Enter a number: "))
#print(x*3)





