class Stack():
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

inp = input("Enter Input : ").split()
S = Stack()
count = 0
for i in inp:
    S.push(i)
    if (S.size() >= 3) and (S.items[-1] == S.items[-2] == S.items[-3]):
        S.pop()
        S.pop()
        S.pop()
        count += 1
print(S.size())
if S.is_empty():
    print("Empty")
if count > 1:
    print(f"Combo : {count} ! ! !")
print("".join(reversed(S.items)))