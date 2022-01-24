

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
        new_node.next = self.head
        self.head = new_node 
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


    def get(self,index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp 


    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value 
            return True 
        return False 

    def count(self, value):
        counts = 0
        current = self.head 
        while (current is not None):
            if current.value == value:
                counts += 1 
            current = current.next 
        return counts

    

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next 
        temp.next = new_node 
        self.length += 1 
        return True  


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.prepop()
        if index == self.length:
            return self.pop()  
        pre = self.get(index - 1)
        temp = pre.next 
        pre.next = temp.next
        temp.next = None 
        self.length -= 1
        return temp 

    def reverse(self):
        temp = self.head 
        self.head = self.tail 
        self.tail = temp 
        after = temp.next 
        before = None 
        for _ in range(self.length):
            after = temp.next 
            temp.next = before 
            before = temp 
            temp = after 

my = LinkList(0)
my.append(1)
my.append(2)
my.append(3)
my.set_value(0,1)
my.reverse()
my.print_list()
print(f"number of times {my.count(1)}")


