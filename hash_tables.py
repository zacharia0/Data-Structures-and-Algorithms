class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size 


    def __hash(self, key):
        my_hash = 0 
        for letter in str(key):
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")

    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


my = HashTable()

my.set_item("bolts", 1400)
my.set_item("washers", 50)
my.print_table()