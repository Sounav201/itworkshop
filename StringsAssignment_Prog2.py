def rev(str):
    words=str.split(' ')
    res=' '.join(reversed(words))
    return res



str=input("Enter a sentence ")
res=rev(str)

print(res)