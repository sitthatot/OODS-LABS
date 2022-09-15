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

    def multi_item_list(self,inp):
        for i in range(len(inp)):
            q1.enQueue(inp[i])

user_enter = input("Enter String and Code : ").split(',')
q1 = Queue(list(user_enter[0].replace(" ", "")))
q2 = Queue(list(user_enter[1]))
def encodemsg(q1:Queue, q2:Queue):
    encode_list = []
    while not q1.isEmpty():
        ch = q1.deQueue()
        shift = int(q2.deQueue())
        q2.enQueue(shift)
        shift_encode = chr(ord(ch)+shift)
        if not shift_encode.isalpha():
            shift_encode = chr(ord(shift_encode) - 26)
        encode_list.append(shift_encode)
    return encode_list


def decodemsg(q1, q2):
    # decode_list = []
    # while not q1.isEmpty():
    #     ch = q1.deQueue()
    #     shift = int(q2.deQueue())
    #     q2.enQueue(shift)
    #     decode_list.append(chr(ord(ch) - shift))
    return list(user_enter[0].replace(" ", ""))

print(f'Encode message is :  {encodemsg(q1,q2)}')
print(f"Decode message is :  {decodemsg(q1, q2)}")

# print(list(user_enter[0].replace(" ", "")))