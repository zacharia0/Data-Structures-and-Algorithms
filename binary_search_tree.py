class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 



class BinarySearchTree:
    def __init__(self):
        self.root = None 


    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root 
        while (True):
            if new_node.value ==  temp.value:
                return False 
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left 
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True 
                temp= temp.right 


    def contains(self,value):
        temp = self.root
        while temp is not None: 
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right 
            else:
                return True
        return False  


    def minimum_value_left(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left 
        return current_node

    def maximum_value_right(self, current_node):
        while current_node.right is not None:
            current_node =  current_node.right
        return current_node







