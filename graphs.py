class Graph:
    def __init__(self):
        self.adjancency_list = {}

    def print_graph(self):
        for vertex in self.adjancency_list:
            print(f"{vertex} : {adjancency_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex is not in self.adjancency_list.keys():
            self.adjancency_list[vertext] = []
            return True 
        return False 