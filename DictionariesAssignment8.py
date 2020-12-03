d1={'a':20 ,'b':10  , 'c':30 , 'd':40}

print("Initial dictionary :  " + str(d1))

d1_inv=dict(map(reversed, d1.items()))

print("Inverted dictionary : "  + str(d1_inv)  )


