def volume(l=1,b=1,h=1):
    return l*b*h


length=int(input("Enter the length   of the box  "))
breadth=int(input("Enter the breadth of the box  "))
height=int(input("Enter the height   of the box  "))


vol1=volume(length,breadth,height)

vol2=volume(length,breadth)

vol3=volume(length)

vol4=volume()

print(vol1)
print(vol2)
print(vol3)
print(vol4)

