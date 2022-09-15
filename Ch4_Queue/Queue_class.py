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

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

my_list = ['a','b','c']
queue = Queue(my_list)
queue.enQueue('d')
queue.enQueue('HASHA')
print(queue.items)
queue.deQueue()
print(queue.items)
queue.deQueue()
print(queue.items)
print(queue.deQueue())
print(queue.items)
print(queue.peek())
print(queue.size())
print(queue.is_empty())