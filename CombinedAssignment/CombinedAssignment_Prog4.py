s=['1','2','3','4','5','6','7','8','9','10','11']


while True:
    print('Do you want to enter the indexes ? Type index')
    print('Exit')

    ch=input(('Enter the operation you want to do ')).split()

    choice= ch[0].strip().lower()

    if choice=='exit':
        break
    elif choice=='index':


        start=int(input('Enter the starting index from which you want to slice '))

        end=int(input('Enter the last index to which you want to slice '))
        print(s[start:end])
    else:
        print("Invalid Input. Please try again ")

