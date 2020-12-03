dictionary={'a':100 ,
            'b':200 ,
            'c':300 ,
            'd':400 ,}

max_key= max(dictionary.keys(), key= (lambda i: dictionary[i]))
min_key= min(dictionary.keys(), key= (lambda i:dictionary[i]))

print("Maximum value : " , dictionary[max_key])
print("Minimum value : " , dictionary[min_key])
