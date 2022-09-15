class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def head_change(self):
        if self.head.value == "0":
            return
        curr = self.head
        while str(curr.next) != "0":
            curr = curr.next
        new_head = curr.next
        curr.next = None
        self.tail.next = self.head
        self.tail = curr
        self.head = new_head

    def __str__(self):
        if self.head is None:
            return ""
        out = str(self.head)
        current = self.head.next
        while current is not None:
            out += " <- " + str(current)
            current = current.next
        return out

print(" *** Locomotive ***")
user = input("Enter Input : ").split()
linklist = LinkLists()
for i in user:
    linklist.append(i)
print(f"Before : {linklist}")
linklist.head_change()
print(f"After : {linklist}")







