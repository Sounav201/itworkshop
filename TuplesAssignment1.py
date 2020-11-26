tup=(1,2,3)
print(tup)

tup1=(1,2,3)
next=(10,20,30)
new=tup1+next
print(new)


tup2=(5,)
tup2=tup2*5
print(tup2)

tup3=(1,2,3,10,20,30)
print(tup3[2:4])


tup6=(1,2,3)
newlist=list(tup6)
print(newlist)

tup4=(1,2,3,4,5)
max(tup4)
min(tup4)
len(tup4)


#Prog1
#create a tuple
x = ("w3resource")
# Reversed the tuple
y = reversed(x)
print(tuple(y))
#create another tuple
x = (5, 10, 15, 20)
# Reversed the tuple
y = reversed(x)
print(tuple(y))

#Prog2
num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
if isinstance(n, tuple):
break
ctr += 1
print(ctr)


#Prog3

#create a tuple
tuplex = tuple("index tuple")
print(tuplex)
#get index of the first item whose value is passed as parameter
index = tuplex.index("p")
print(index)
#define the index from which you want to search
index = tuplex.index("p", 5)
print(index)
#define the segment of the tuple to be searched
index = tuplex.index("e", 3, 6)
print(index)
#if item not exists in the tuple return ValueError Exception
index = tuplex.index("y")




#create a tuple
tuplex1 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
slice = tuplex1[3:5]
#is exclusive
print(slice)
#if the start index isn&#39;t defined, is taken from the beg inning of the tuple
slice = tuplex1[:6]
print(slice)
#if the end index isn&#39;t defined, is taken until the end of the tuple
slice = tuplex1[5:]
print(slice)
#if neither is defined, returns the full tuple
slice = tuplex1[:]
print(slice)
#The indexes can be defined with negative values
slice = tuplex1[-8:-4]
print(slice)
#create another tuple
tuplex1 = tuple("HELLO WORLD")
print(tuplex1)
#step specify an increment between the elements to cut of the tuple

#tuple[start:stop:step]
slice = tuplex1[2:9:2]
print(slice)
#returns a tuple with a jump every 3 items
slice = tuplex1[::4]
print(slice)
#when step is negative the jump is made back
slice = tuplex1[9:2:-4]
print(slice)






