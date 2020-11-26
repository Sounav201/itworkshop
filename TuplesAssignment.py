def binary_search(a,low,high,key):
    if high>=low:
        mid=(high+low)//2
        if a[mid]==key:
            return mid
        elif a[mid]>key:

            return binary_search(a,low,mid-1,key)

        else :

            return binary_search(a,mid+1,high,key)

    else:
        return -1


def linear_search(a,key):
    for i in range(len(a)):
        if a[i]==key:
            return i

    return -1


a=(10,20,30,40,50,60,70,80,110,145)



choice=int(input("Enter 1 to search using Binary Search. \nEnter 2 to search for an element using Linear Search "))

if choice==1:
    key=int(input(" You have chosen Binary Search . Enter the search element "))
    res=binary_search(a,0,len(a)-1,key)
    if(res==-1):

        print("Element is not found!")
    else:
        print("Element present at  position " + str(res + 1))
if choice==2:
    key = int(input("You have chosen Linear Search . Enter the search element "))

    res=linear_search(a,key)
    if res==-1:
        print("Element is not found!")

    else:
        print("Element present at  position " + str(res + 1))
