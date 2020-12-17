def maxmin(n1,n2,n3):

    if(n1>=n2 and n1>=n3):
        print("Maximum of the three numbers : ", n1)
    elif(n2>=n3 and n2>=n1):
        print("Maximum of the three numbers : ", n2)
    else:
        print("Maximum of the three numbers : " , n3)

    print("Minimum of the three numbers : ", min(n1, n2, n3))



n1=int(input("Enter 1st number  "))
n2=int(input("Enter 2nd number  "))
n3=int(input("Enter 3rd number  "))

maxmin(n1,n2,n3)




