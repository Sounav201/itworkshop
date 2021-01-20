f1=open("demo.txt","w+")
s1='Hello\n'
s2='This is Sounav\n'
s3="I am currently studying in St Thomas' College of Engineering & Technology\n"
lst=[s1,s2,s3]
f1.writelines(lst)

f1.close()

with open('demo.txt') as readf, open('demorev.txt', 'w') as writef:
    for line in reversed(readf.readlines()):
        writef.write(line)
        


        
