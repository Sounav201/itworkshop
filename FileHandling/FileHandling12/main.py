fnames = ['file2.txt', 'file1.txt'] 

with open('cpfile.txt' ,'w') as comp:

    for i in fnames:
        with open(i) as f:
            comp.write(f.read())

        comp.write('\n')

        



    
