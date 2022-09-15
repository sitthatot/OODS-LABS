class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

mylist = ["a","b","c"]
stack = Stack(mylist)
stack.push("CheezeCake")
print(stack.items)
stack.pop()
print(stack.items)
stack.pop()
print(stack.items)
stack.push("HAHAHAAHAHHA")
print(stack.items)
print(stack.is_empty())
stack.pop()
stack.pop()
stack.pop()
print(stack.items)
print(stack.size())
