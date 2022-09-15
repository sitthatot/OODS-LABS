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

def dec2bin(decnum):
    s = Stack()
    number = ""
    reverseNumber = ""
    while decnum != 0:
        binary = int(decnum) % 2
        s.push(binary)
        decnum = int(int(decnum) / 2)
    for bi in s.items:
        number += str(bi)
    for reverseItem in number:
        reverseNumber += str(s.items.pop())
    return reverseNumber
print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))
