class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if self.head is None:
            self.head = Node(item) # append
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def __str__(self):
        if self.head is None:
            return ""
        out = str(self.head)
        current = self.head.next
        while current is not None:
            out += " <- " + str(current)
            current = current.next
        return out

    def move_head(self):
        if self.head.value == "0":
            return
        current_index = self.head
        while str(current_index.next) != "0":
            current_index = current_index.next
        new_head = current_index.next #ชี้ที่ 0
        current_index.next = None #ตัดออก
        self.tail.next = self.head
        self.tail = current_index
        self.head = new_head

print(" *** Locomotive ***")
user = input("Enter Input : ").split()
linklist = LinkedLists()
for i in user:
    linklist.append(i)
print(f"Before : {linklist}")
linklist.move_head()
print(f"After : {linklist}")



