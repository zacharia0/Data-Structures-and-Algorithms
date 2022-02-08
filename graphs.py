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

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass 
        return False 

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for othervertex in self.adjacency_list[vertex]:
                self.adjacency_list[othervertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True 
        return False 
                

            


   
my = Graph()

my.add_vertex("A")
my.add_vertex("B")
my.add_vertex("C")
my.add_vertex("D")


my.add_edge("A","B")
my.add_edge("C","D")
my.add_edge("C","A")
my.add_edge("B","D")
my.add_edge("A","D")
my.print_graph()
print("________________________")
my.remove_vertex("D")
my.print_graph()
# my.remove_edge("A","B")
# my.remove_edge("A","D")
# my.print_graph()
