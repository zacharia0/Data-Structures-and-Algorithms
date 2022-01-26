# class Node:
#     def __init__(self,value):
#         self.value = value 
#         self.next = None 
#         self.prev = None 

# class DoublyLinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1 


# def print_list(self):
#     temp = self.head 
#     while temp is not None:
#         print(temp.value)
#         temp = temp.next 

# def append(self, value):
#     new_node = Node(value)
#     if self.length == 0:
#         self.head = new_node
#         self.tail = new_node
#     else:
#         self.tail.next = new_node
#         new_node.prev = self.tail 
#         self.tail = new_node
#     self.length += 1 
#     return True 


# def pop(self):
#     if self.length == 0:
#         return 0
#     temp = self.tail 
#     if self.length == 1:
#         self.head = None 
#         self.tail = None 
#     else:
#         self.tail = self.tail.prev 
#         self.tail.next = None 
#         temp.prev = None 
#     self.length -= 1 
#     return temp 




class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 



class DoublyLinkedList:
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

    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        self.length += 1
        return True 

    
    def pop(self):
        if self.length == 0:
            return None 
        if self.length == 1:
            self.tail = None 
            self.head = None 
        else:
            temp = self.tail 
            self.tail = self.tail.prev 
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1
        return temp  


    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
        self.length += 1 
        return True 


    def prepop(self):
        if self.length == 0:
            return None 
        temp = self.head
        if self.length == 1:
            self.tail = None 
            self.head = None 
         
        else:
            self.head = self.head.next 
            self.head.prev = None 
            temp.next = None 
        self.length -= 1 
        return temp 
         


my = DoublyLinkedList(0)
my.append(1)
my.append(2)
my.prepop()
my.prepop()
my.prepop()
my.print_list()