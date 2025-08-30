class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        # For undirected graph
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  

    def display(self):
        for row in self.adj_matrix:
            print(row)

# Example usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.display()