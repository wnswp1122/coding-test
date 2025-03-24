class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
        
    def get_node(self, index):
        node = self.head
        cur_index = 0

        while cur_index < index:
            cur_index += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)

        if(index == 0):
            new_node.next = self.head
            self.head = new_node  
            return   
        node = self.get_node(index - 1)
        temp = node.next
        node.next = new_node
        new_node.next = temp

    def delete_node(self, index):
        if(index == 0):
            self.head = self.head.next
            return 
        self.get_node(index - 1).next = self.get_node(index).next
    
linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.delete_node(1)
linked_list.print_all()     