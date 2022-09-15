class Stack:
    """
    class Stack
    default : empty stack / stack([...])
    """
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


inp = input('Enter Infix : ')

S = Stack()
opdict = {
    '(': 0,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3
}

print('Postfix : ', end='')
### Enter Your Code Here ###
for e in inp:
    if e.isalpha():
        print(e,end='')
    else:
        if e == '(':
            S.push(e)
        elif e == ')':
            while S.peek() != '(':
                print(S.pop(),end='')
            S.pop()
        elif S.isEmpty() or opdict[e] > opdict[S.peek()]:
            S.push(e)
        else:
            while not S.isEmpty() and S.peek() != '(' and opdict[S.peek()] >= opdict[e]:
                print(S.pop(),end='')
            S.push(e)


while not S.isEmpty():
    print(S.pop(), end='')
print()