Student={
'id1':
{"name": ["Ron"],
 "class": ['X'],
 "subjects": ["Maths","Physics", "English"]
},

'id2':
{"name": ["Shane"],
 "class": ['XII'],
 "subjects": ["History","Chemistry", "English"]
},

'id3':
{"name": ["Robie"],
 "class": ['XII'],
 "subjects": ["Maths","Physics", "Computer"]

},

'id4':
{"name": ["Ron"],
 "class": ['X'],
 "subjects": ["Maths","Physics", "English"]
},

'id5':
{"name": ["Sara"],
 "class": ['IX'],
 "subjects": ["English","Geography", "Biology"]
}
}
#name= input("Enter your name  ")
#cls= input("Enter your class ( IN ROMAN NUMERALS) ")

res={}

for key,value in Student.items():
    if value not in res.values():
        res[key]=value

print(res)




