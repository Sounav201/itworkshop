with open("file.txt") as f1:
    with open("file1.txt" ,"w") as f2:
        for i in f1:
            f2.write(i)

