class Stack :
    def __init__(self, list = None):
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

def dec2bin(decnum):

    s = Stack()
    rev = Stack()
    while decnum != 0:
        s.push(int(decnum)%2)
        decnum = int(decnum)/2
        # rev.push(s.pop())

    answer_notRev = ''.join(str(e) for e in s.items)
    for i in answer_notRev:
        rev.push(s.pop())
    answer = ''.join(str(e) for e in rev.items)
    return answer[1:]

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))