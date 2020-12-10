list_of_words=['Apple' , 'Amazing','Ant','Aeroplane', 'Bat' ,'Baseball','Bake','Bomb','Cameroon','Cost','Claws', 'Cat' , 'Dog' ,'Demon','Dusk','Damp', 'Element' , 'Fish' ,'Fan','Foul','Feather' ]

ls=[]

query=input("Enter an Alphabet ")

for i in range(0,len(list_of_words)):

    letter= list_of_words[i][:1]
    if query==letter:
        print(list_of_words[i])


