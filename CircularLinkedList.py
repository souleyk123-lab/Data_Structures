class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                 cur = cur.next
        cur.next = new_node
        new_node.next = self.head

    def prepend(self, data):
         new_node = Node(data)
         cur = self.head
         new_node.next = self.head
         if not self.head
            new_node.next  = Node
        else: 
            while cur.next != self.head
                cur = cur.next
            cur.next = new_node
        self.head = new_node
        
    def display_list(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            p = self.head
            while p is not None:
                print(p.data)
                p = p.next
                if cur == self.head:
                    break
clsit = CircularLinkedList()
clsit.append("C")
clsit.append("D")
clsit.display_list()
clsit.prepend("A")
clsit.display_list()
