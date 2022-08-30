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

user_enter = input("Enter people and time : ").split(' ')
q1 = Queue(list(user_enter[0]))
q2 = Queue()
q3 = Queue()
q_number = Queue(user_enter[1])
# print(q_number.items)

i = 1
check = 0
checkq3 = 0
while i <= int(q_number.items):
    if checkq3 == 2:
        q3.deQueue()
        checkq3 = 0

    if check == 3:
         q2.deQueue()
         check=0

    if q1.size() != 0 and q2.size() < 5:
        q2.enQueue(q1.deQueue())
    elif q2.size() >= 5 and q1.size() != 0:
        q3.enQueue(q1.deQueue())

    if q2.size() != 0:
        check += 1
    if q3.size() != 0:
        checkq3 += 1
    print(i, q1.items, q2.items, q3.items)
    i += 1