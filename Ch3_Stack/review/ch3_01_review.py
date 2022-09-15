class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

print(" *** Stack implement by Python list***")
user_enter = input("Enter data to stack : ").split()
myStack = Stack()
for data in user_enter:
    myStack.push(data)
print(f"{myStack.size()} Data in stack :  {myStack.items}")

while not myStack.is_empty():
    myStack.pop()
print(f"{myStack.size()} Data in stack :  {myStack.items}")
