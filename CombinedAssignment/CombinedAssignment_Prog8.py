Birthdays={'Nathan':"30/4/1999",
           'Drake':"15/8/2000",
           'Nabarun': "9/2/2001",
           'Adityaprava':"7/11/2001",
           'Saharsha':"24/11/2001",
           'Archisman':'15/6/2000'}


for key in sorted(Birthdays.keys()):
    print(key)

query = input("Who's birthday do you want to look up? ")
result = Birthdays[query] if query in Birthdays else None
if  result == None:
#    print("Enter the record ?")
    d={}
    for i in range(1):
        keys = input('Enter the name ')
        values = input('Enter the Birthday in DD/MM/YY format ')
        d[keys] = values
    Birthdays.update(d)
    print("Birthday Added .")
    print("{}'s birthday is {}".format(query, Birthdays[query]))
else:
    print("{}'s birthday is {}".format(query, Birthdays[query]))





