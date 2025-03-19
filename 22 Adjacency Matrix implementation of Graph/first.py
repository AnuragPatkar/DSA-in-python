class Graph:
    def __init__(self,vertex_count):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for _ in range(vertex_count)]

    def add_edge(self,u,v,weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight

    def remove_edge(self,u,v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0

    def has_edge(self,u,v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            if self.adj_matrix[u][v]!=0:
                return True
            return False
    
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(' '.join(map(str,row)))

