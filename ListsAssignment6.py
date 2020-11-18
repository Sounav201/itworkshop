def compare(ls1,ls2):
    num=sum(a==b for a,b in zip(ls1,ls2))
    return num==len(ls1)==len(ls2)

def difference(ls1,ls2):

    print([x for x in ls1 if x not in set(ls2)])


ls1=[3,2,4,5,7]
ls2=[6,1,4,5,7]

res=compare(ls1,ls2)
if res==False:
    print("We need to find the difference between the two lists ")
    difference(ls1,ls2)
else:
    print("Both lists are same!")
