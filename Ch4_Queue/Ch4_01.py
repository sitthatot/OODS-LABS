class Stack:

    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def multi_item_list(self,inp):
        for i in range(len(inp)):
            queue.enQueue(inp[i])
queue = Queue()
user_input = input("Enter Input : ").split(',')
# print(user_input)
for i in range(len(user_input)):
    user_input_inside = user_input[i].split(' ')
    # print(user_input_inside)
    if user_input_inside[0] == 'E':
        queue.enQueue(user_input_inside[1])
        print(f"Add {user_input_inside[1]} index is {queue.size()-1}")
    elif user_input_inside[0] == 'D':
        if queue.size() != 0:
            print(f"Pop {queue.deQueue()} size in queue is {queue.size()}")
        else:
            print('-1')
if queue.size() != 0:
    print(f"Number in Queue is :  {queue.items}")
else:
    print("Empty")



