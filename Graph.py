class Graph:
    def __init__(self):
        self.adjacency_list = {} #dictionary -> key (address/vertex) and values (list of vertices)
  
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = [] #list of vertices

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)