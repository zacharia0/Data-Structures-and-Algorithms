class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 



class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def print_binary_search_tree_right(self):
        temp = self.root.right
        while temp is not None:
            print(temp.value)
            temp = temp.right 
    
    def print_binary_search_tree_left(self):
        temp = self.root.left
        while temp.left is not None:
            print(temp.value)
            # temp = temp.left 

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True 
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True 
                temp = temp.left 
            else:
                if new_node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        return True 
                    temp = temp.right 


