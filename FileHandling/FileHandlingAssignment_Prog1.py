f1=open("file.txt","w+")
s1='Hello\n'
s2='This is Sounav\n'
s3="I am currently studying in St Thomas' College of Engineering & Technology\n"
lst=[s1,s2,s3]
f1.writelines(lst)

f1.close()
f1=open("file.txt","r")
lines=f1.readlines()
count=0
for line in lines:
    print(line)

f1.seek(0)


print(f1.read(5))
f1.close()

f1=open("file.txt" ,'a+')
s4="Line1 is appended\n"
s5="Line2 is appended\n"
ls=[s4,s5]
f1.writelines(ls)

f1.close()








