class node:
    def __init__(self,data,next = None ):
        self.prev = None
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0])
    curr = head
    for i in range(1,len(l)):
        new_node = node(l[i])


def printList(H):
    pass

def mergeOrderesList(p,q):
    pass

    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ', end='')
    printList(LL1)
    print('LL2 : ', end='')
    printList(LL2)
    m = mergeOrderesList(LL1, LL2)
    print('Merge Result : ', end='')
    printList(m)