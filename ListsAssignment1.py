players=['Adam', 'Ben' ,'Charles', 'David']
p=['Lampard','Scholes', 'Viera', 'Fabregas', 'Gerrard']

players.extend(p)
for i in range(5):

    player=input("Enter the name of the player you want to add to the list ")
    players.append(player)
    print("Player added. ")

print(players)
