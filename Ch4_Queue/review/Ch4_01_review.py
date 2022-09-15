class Queue:
    def __init__(self, list = None):
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

user_enter = input("Enter Input : ").split(",")
print(user_enter[0][1])
# myQueue = Queue()
# if user_enter[0][0] == "E":
#     myQueue.enQueue()

