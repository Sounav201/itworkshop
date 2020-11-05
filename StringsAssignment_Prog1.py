def palindromecheck(str):
    strrev=str[::-1]
    if strrev==str:
        return True
    else:
        return False


str=input("Enter a word to find if it is a palindrome or not. ")
res=palindromecheck(str)

if res==True:
    print(str + " is a Palindrome!")
else:
    print(str + " is not a Palindrome!")


