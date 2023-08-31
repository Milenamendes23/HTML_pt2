class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.hand    
        self.head = new_node

    def print_reverse(self,node):
        if node is None:
            return
        self.print_reverse(node.next)
        print (node.data, end= " ")
    
    def print_list_reverse(self):
        self.print_reverse(self.head)
    
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    
    print("Lista a partir do final:")
    llist.print_list_reverse()