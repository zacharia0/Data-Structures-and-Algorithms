class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")


    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True 
        return False 

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True 
        return False

my = Graph()

my.add_vertex("A")
my.add_vertex("B")

my.add_edge("A","B")
my.print_graph()
