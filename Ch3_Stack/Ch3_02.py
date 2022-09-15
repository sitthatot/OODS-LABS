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

s = Stack()
user_enter = input("Enter expresion : ")
list(user_enter)

for i in range(len(user_enter)):
    if user_enter[i] == '{' or user_enter[i] == '}'or user_enter[i] == '['or user_enter[i] == ']'or user_enter[i] == '('or user_enter[i] ==')':
        s.push(user_enter[i])
s.items = ''.join(s.items)

stack = Stack()
check = True

for i in range(len(s.items)):
    if s.items[i] == '{' or  s.items[i] == '[' or s.items[i] == '(':
        stack.push(s.items[i])
    try:
        if s.items[i] == '}':
            if stack.pop() != '{':
                print(user_enter + " Unmatch open-close")
                check = False
                break

        elif s.items[i] == ']':
            if stack.pop() != '[':
                print(user_enter + " Unmatch open-close")
                check = False
                break

        elif s.items[i] == ')':
            if stack.pop() != '(':
                print(user_enter + " Unmatch open-close")
                check = False
                break
    except:
        print(user_enter + " close paren excess")
        check = False
        break

if check:
    if len(stack.items) != 0:
        print(user_enter + " open paren excess   " + str(len(stack.items)),end=' : ')
        for item in stack.items:
            print(item,end='')
    else :
        print(user_enter + " MATCH")



