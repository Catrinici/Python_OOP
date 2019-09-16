class SLNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:
    def __init__(self,value):
        self.head = None
        self.tail = None


list = SList()
list.head = SLNode("Antonita")
list.head.next = SLNode("Nelutu")
list.head.next.next = SLNode("Mihaita")
