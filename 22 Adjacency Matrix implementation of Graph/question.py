# Assignment-22: Adjacency Matrix implementation of Graph

""" # 1. Write a class Graph to implement adjacency matrix representation of a simple and undirected graph.
class Graph:
    def __init__(self,vertex_count):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for _ in range(vertex_count)] """

""" # 2. In class Graph, define _init_ method to initialise vertex_count and adj_matrix (list of lists)
    def __init__(self,vertex_count):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for _ in range(vertex_count)] """

""" # 3. In class Graph, define add_edge() method add an edge in the graph with given weight.
    def add_edge(self,u,v,weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight """

""" # 4. In class Graph, define remove_edge() method to remove an edge from the graph.
    def remove_edge(self,u,v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0 """

""" # 5. In class Graph, define has_edge() method to check whether two given vertices are connected by an edge or not.
    def has_edge(self,u,v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            if self.adj_matrix[u][v]!=0:
                return True
            return False """

""" # 6. In class Graph, define print_adj_matrix() method to print adjacency matrix
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(' '.join(map(str,row))) """