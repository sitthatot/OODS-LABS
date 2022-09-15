class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,data):
        self.items.append(data)

    def deQueue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

user_enter = input("Enter people and time : ").split()
q1 = Queue(list(user_enter[0]))
q2 = Queue()
q3 = Queue()
q_number = Queue(user_enter[1])

i = 1
checkq2 = 0
checkq3 = 0
while i <= int(q_number.items):
    if checkq3 == 2:
        q3.deQueue()
        checkq3 = 0

    if checkq2 == 3:
        q2.deQueue()
        checkq2 = 0

    if q1.size() != 0 and q2.size() < 5:
        q2.enQueue(q1.deQueue())
    elif q1.size() != 0 and q2.size() >= 5:
        q3.enQueue(q1.deQueue())

    if q2.size() != 0:
        checkq2 += 1
    if q3.size() != 0:
        checkq3 += 1
    print(i, q1.items, q2.items, q3.items)
    i += 1
