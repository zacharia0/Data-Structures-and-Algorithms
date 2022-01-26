


class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
        self.previous = None 

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            new_node.previous = self.tail 
            self.tail = new_node 
        self.length += 1 
        return True 



my = DoublyLinkedList(0)
my.push(1)
my.print_list()