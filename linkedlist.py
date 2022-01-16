from hashlib import new

from matplotlib.pyplot import get


class Node:
    """The Node class creates a node""" 
    def __init__(self,value):
        """Initialize the constructor"""
        self.value = value 
        self.next = None 

class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1
        return True 
    

    def pop(self):
        if self.length == 0:
            return None 

        temp = self.head 
        pre = self.head 

        while temp.next is not None:
            pre = temp 
            temp = temp.next 

        self.tail = pre 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp 

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 

        self.head = new_node 
        new_node.next = self.head 
        self.length += 1 
        return True 


    def prepop(self):
        if self.length == 0:
            return None
        temp = self.head 
        self.head = self.head.next 
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None 
        return temp 


        
    


    