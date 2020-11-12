def count(sent):
    vowels=0
    cons=0
    punc=0
    for i in range(0,len(sent)):
        ch=sent[i]
        if ( (ch >='a' and ch<='z') or (ch>='A' and ch<='Z')):

            if sent[i]=='a' or sent[i]=='e' or sent[i]=='o' or sent[i]  =='u' or sent[i]=='i':
                vowels+=1
            else:
                cons+=1
        if (ch=='.' or ch=='?' or ch=='!' or ch==':' or ch==';' or ch==','):

            punc+=1

    words=len(sent.split())
    print("The number of vowels : " +  str(vowels) )
    print("The number of consonants : " + str(cons))
    print("The number of words :  " + str(words))
    print("The number of punctuation : " + str( punc))



sent=input("Enter a sentence ")
count(sent)



