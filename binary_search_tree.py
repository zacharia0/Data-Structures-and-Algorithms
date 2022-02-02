class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 



class BinarySearchTree:
    def __init__(self):
        self.root = None 


#     def insert(self,value):
#         new_node = Node(value)
#         if self.root == None:
#             self.root = new_node
#             return True 
#         temp = self.root
#         while (True):
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True 
#                 temp = temp.left 
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True 
#                 temp = temp.right 

#     def contains(self,value):
#         if self.root == None:
#             return False  
#         temp = self.root 
#         while temp is not None:
#             if value < temp.value:
#                 temp = temp.left 
#             elif value > temp.value:
#                 temp = temp.right
#             else:
#                 return True 
#             return False  
            
# my = BinarySearchTree()
# my.insert(4)
# my.insert(5)
# print(my.contains(1))



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


    def minimum_value(self, current_node):
        while current_node.left is not None:
            current = current_node.left 
        return current_node








