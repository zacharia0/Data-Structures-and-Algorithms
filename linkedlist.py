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
        




