class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur is not None:
                cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    def display_list(self):
        cur = self.head 
        while cur:
            print(cur.data)
            cur = cur.next
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

dlist = DoubleLinkedList()
dlist.append("A")
dlist.append("B")
dlist.append(2)
dlist.append(45)
dlist.display_list()