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
        return current_node.value

    def maximum_value_right(self, current_node):
        while current_node.right is not None:
            current_node =  current_node.right
        return current_node



    ################### TREE TRAVERSAL ##############################################
    def BFS(self):
        current_node = self.root 
        queue = [] 
        result = [] 
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result 


    def dfs_pre_order(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result 





my = BinarySearchTree()
my.insert(47)
my.insert(21)
my.insert(76)
my.insert(18)
my.insert(27)
my.insert(52)
my.insert(82)
print(my.dfs_pre_order())