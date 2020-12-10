class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return  self.items[len(self.items)-1]

    def size(self):
        return  len(self.items)


s= Stack()

while True:
    print('push element into the Stack -> Enter push ')
    print('pop element from the Stack -> Enter pop ')
    print('peek the topmost element in the Stack -> Enter peek ')
    print('Get the size of the Stack  -> Enter size ')
    print('Exit')

    ch=input(('Enter the operation you want to do ')).split()

    choice= ch[0].strip().lower()

    if choice =='push':
        val=int(input("Enter the value you want to push into the stack "))
        s.push(val)
        print(str(val) + " is pushed into the Stack. ")

    elif choice == 'pop':
        if s.isEmpty():
            print('No items to pop! Stack is empty.')
        else:
            print('Popped value: ' , s.pop())
    elif choice == 'peek':
        if s.isEmpty():
            print('No items in the Stack.')
        else:
            print('Topmost value: ' , s.peek())

    elif choice =='size':
        print('Size of the Stack is  ',s.size())

    elif choice == 'exit':
        break
