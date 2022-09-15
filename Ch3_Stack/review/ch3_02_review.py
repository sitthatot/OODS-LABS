class Stack():
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

user_enter = input("Enter expresion : ")
myStack = Stack()
open = "{[("
close = "}])"
try:
    for paren in user_enter:
        if paren == "{" or paren == "[" or paren == "(" or paren == "}" or paren == "]" or paren == ")":
            if paren in open: #วงเล็บเปิด
                myStack.push(paren)
            else: #วงเล็บปิด

                    if open.index(myStack.peek()) == close.index(paren):
                        myStack.pop()
                    else:
                        break

    if myStack.is_empty():
        print(f"{user_enter} MATCH")
    else: #ไม่ว่าง
        print(f'{user_enter} open paren excess   {myStack.size()} : {"".join(myStack.items)}')

except:
    print(f"{user_enter} close paren excess")