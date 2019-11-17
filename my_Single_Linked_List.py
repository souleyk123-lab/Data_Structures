class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            return True
        else:
            False
    def add_to_start(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def add_to_end(self, data):
        node = Node(data)
        p = self.head
        while p is not None:
            p = p.next
        p.next = node
    def insert_before_a_node(self, position, data):
        node = Node(data)
        p = self.head
        while p.next is not None:
            if p.next.data == position:
                node.next = p.next
                p.next = node
            p = p.next
    def insert_after_a_node(self, position, data):
        node = Node(data)
        p = self.head
        while p is not None:
            if p == position:
                node.next = p.next
                p.next = node
    def delete_a_node(self, node):
        p = self.head
        while p.next is not None:
            if p.next.data == node:
                break
                p = p.next
            else:
                return False
    def reverse_list(self):
        prev = None
        p = self.head
        while p is not None:
            temp = p
            p = p.next 
            prev = temp 
        return prev
    def print_list(self):
        if self.head is None:
            return list()
        else:
            p = self.head
            result = [] 
            while p is not None:
                result.append(p)
                p = p.next
            return result

s = SingleLinkedList()
s.add_to_start(45)
s.insert_after_a_node(45, 20)
s.insert_after_a_node(20, 40)
s.add_to_end(55)
s.print_list()
s.is_empty 