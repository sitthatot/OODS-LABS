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


user_input = input("Enter Input (Normal, Mirror) : ").split()
# print(user_input)
normal = Queue()
mirror = Stack()
normal_explode = 0
normal_explode_failed = 0
mirror_queue = Queue()
mirror_explode = 0
for i in reversed(user_input[1]):
    mirror.push(i)
    if (mirror.size() >= 3) and ((mirror.items[-1] == mirror.items[-2] == mirror.items[-3])):
        mirror_queue.enQueue(mirror.pop())
        mirror.pop()
        mirror.pop()
        mirror_explode += 1

# print(mirror.items)
# print(mirror_queue.items)

for i in user_input[0]:
    normal.enQueue(i)
    # print(normal.items)
    if (normal.size() >= 3) and (normal.items[-1] == normal.items[-2] == normal.items[-3]) and not mirror_queue.isEmpty():
        temp_pop = normal.items.pop()
        # print(temp_pop)
        # print(mirror_queue.deQueue())
        normal.enQueue(mirror_queue.deQueue())
        normal.enQueue(temp_pop)
        # print(normal.items)
        if (normal.items[-1] == normal.items[-2] == normal.items[-3]):
            normal.items.pop()
            normal.items.pop()
            normal.items.pop()
            normal_explode_failed += 1
    else:
        if (normal.size() >= 3) and (normal.items[-1] == normal.items[-2] == normal.items[-3]):
            normal.items.pop()
            normal.items.pop()
            normal.items.pop()
            normal_explode += 1

print("NORMAL :")
print(normal.size())
if normal.size() == 0:
    print('Empty')
else:
    print(''.join(reversed(normal.items)))
print(f'{normal_explode} Explosive(s) ! ! ! (NORMAL)')
if normal_explode_failed != 0:
    print(f'Failed Interrupted {normal_explode_failed} Bomb(s)')

print('------------MIRROR------------')
print(': RORRIM')
print(mirror.size())
if mirror.size() == 0:
    print("ytpmE")
else:
    print(''.join(reversed(mirror.items)))
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirror_explode}')
