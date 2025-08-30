from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        # Undirected graph → add both ways
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        for node in self.adj_list:
            print(node, "→", self.adj_list[node])

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.display()