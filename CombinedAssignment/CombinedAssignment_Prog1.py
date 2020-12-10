list_of_words=['Apple' , 'Amazing','Ant','Aeroplane', 'Bat' ,'Baseball','Bake','Bomb','Cameroon','Cost','Claws', 'Cat' , 'Dog' ,'Demon','Dusk','Damp', 'Element' , 'Fish' ,'Fan','Foul','Feather' ]

ls=[]


for i in range(0,len(list_of_words)):

    ls.append(list_of_words[i][:1])


print(ls)



