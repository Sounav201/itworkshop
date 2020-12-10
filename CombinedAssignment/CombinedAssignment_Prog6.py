EmployeeData = {'emp1': {'name': 'Sam', 'job': 'UI Developer' , 'DateOfJoining':'18-11-2019' , 'salary':'40000'},
     'emp2': {'name': 'John', 'job': 'Back-End Developer' , 'DateOfJoining':'25-06-2020' , 'salary':'50000'},
     'emp3': {'name': 'Ryan', 'job': 'Cyber Security Cell' , 'DateOfJoining':'08-01-2018' ,'salary':'60000'},
     'emp4': {'name': 'Kate', 'job': 'Android Developer' , 'DateOfJoining':'21-07-2017' ,'salary':'55000'},
     'emp5': {'name': 'Abhiraj', 'job': 'Full-Stack Web Developer' , 'DateOfJoining':'06-08-2020' , 'salary':'80000'},
     'emp6': {'name': 'Sarah', 'job': 'Manager', 'DateOfJoining': '15-04-2018' , 'salary':'85000'}}


while True:
    print('Enter the employee ID -> (For eg: emp1) ')
    print('Exit')

    ch=input(('Enter the operation you want to do ')).split()

    choice= ch[0].strip().lower()

    if choice=='exit':
        break
    else:
        options=input("Type Y if you want to see all the information of the employee. Type N if you want to see a particular field ").split()
        option = options[0].strip().lower()
        if option=='y':
            print(EmployeeData[choice])
        elif option=='n':
            field=input("Enter the field which you want to see  -> name , job , DateOfJoining , salary  ").split()
            ans=field[0].strip().lower();

            print(EmployeeData[choice].get(ans))





