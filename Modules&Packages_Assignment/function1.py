def f1(x,y):
    if(y<=x):
        return int(f1(x-y,y)) + 1

    return 1

         