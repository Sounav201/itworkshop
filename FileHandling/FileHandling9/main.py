import filecmp
f1=open("file1.txt","w+")
s1='Hello\n'
s2='This is Sounav\n'
s3="I am currently studying in St Thomas' College of Engineering & Technology\n"
lst=[s1,s2,s3]
f1.writelines(lst)

f1.close()

f1=open("file2.txt","w+")
s1='Hello\n'
s2='This is Sounav\n'
s3="I am currently studying in St Thomas' College of Engineering & Technology\n"
lst=[s1,s2,s3]
f1.writelines(lst)

f1.close()

F1='file1.txt'
F2='file2.txt'

comp=filecmp.cmp(F1,F2)
print(comp)


