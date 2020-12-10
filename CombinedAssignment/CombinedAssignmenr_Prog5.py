ls=[1,2,3,4,5,7,8,(12,13),15,16]

j=0

for i in ls:
    if isinstance(i,tuple):
        break
    j+=1

print(j)
