class Node:
    def __init__(self, data):
        self.prev: "Node" = None
        self.data = data
        self.next: "Node" = None

    def __str__(self):
        return str(self.data)


class Doubly_Linked_List:
    def __init__(self):
        self.head: "Node" = None
        self.tail: "Node" = None

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
        else:
            n = Node(data)
            self.tail.next = n #ชี้ไปที่ Node ใหม่
            n.prev = self.tail #Node ใหม่ชี้ไปที่ Tai'
            self.tail = n #เปลี่ยน Tail ให้เป็น Tail ที่ Node ใหม่

    def add_before(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
        else:
            n = Node(data)
            self.head.prev = n
            n.next = self.head
            self.head = n

    def __str__(self):
        ret = []
        curr = self.head
        # total_string = ""
        while curr is not self.tail:
            # total_string += curr.data
            ret.append(str(curr.data))
            curr = curr.next
        if self.tail is not None:
            # total_string += self.tail.data
            ret.append(str(self.tail.data))
        # return total_string
        return "->".join(ret)

    def str_reverse(self):
        ret = []
        curr = self.tail
        # total_string = ""
        while curr is not self.head:
            # total_string += curr.data
            ret.append(str(curr.data))
            curr = curr.prev
        if self.head is not None:
            # total_string += self.head.data
            ret.append(str(self.head.data))
        return "->".join(ret)

    def insert(self,index,data):
        if index == 0:
            self.add_before(data)
        elif index < 0:
            return
        else:
            curr = self.head
            for i in range(index-1):
                if curr is None:
                    return
                curr = curr.next
            if curr is None:
                return
            n = Node(data)
            n.next = curr.next
            curr.next.prev = n
            n.prev = curr
            curr.next = n
    def remove(self,data):
        curr = self.head
        while curr != None and (curr.data != data):
            curr = curr.next
        if curr is None:
            print("Not Found!")
            return
        if curr.prev is not None:
            curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        if curr is self.head:
            self.head = curr.next
        if curr is self.tail:
            self.tail = curr.prev

mydoub = Doubly_Linked_List()
inp = input("Enter Input : ").replace(", ",",").split(",")
for i in range(len(inp)):
    # print(inp[i][2:])
    if inp[i][0:2] == "A ":
        mydoub.append(inp[i][2:])
        print(f"linked list : {mydoub}")
        print(f"reverse : {mydoub.str_reverse()}")
    if inp[i][0:3] == "Ab ":
        mydoub.add_before(inp[i][3:])
        print(f"linked list : {mydoub}")
        print(f"reverse : {mydoub.str_reverse()}")
    if inp[i][0:2] == "I ":
        splitter = inp[i][2:].split(":")
        if splitter[0][0] == "-":
            print("Data cannot be added")
            print(f"linked list : {mydoub}")
            print(f"reverse : {mydoub.str_reverse()}")
        else:
            mydoub.insert(int(splitter[0]),int(splitter[1]))
            print(f"index = {splitter[0]} and data = {splitter[1]}")
            print(f"linked list : {mydoub}")
            print(f"reverse : {mydoub.str_reverse()}")
    if inp[i][0:2] == "R ":
        mydoub.remove(inp[i][2:])
        print(f"removed : {inp[i][2:]} from index : {i}")
        print(f"linked list : {mydoub}")
        print(f"reverse : {mydoub.str_reverse()}")

