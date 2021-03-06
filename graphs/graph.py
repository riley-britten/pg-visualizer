class graph:
    def __init__(self, n, edges, isDirected):
        """
        Vertices are always named 1 .. n
        edges are stored as a set of tuples.
        Undirected graphs are represented by setting
        the isDirected flag to False and considering
        all edges to be bidirectional.

        Example of a 1 vertex undirected graph:
        graph(1, set(()), False)

        Example of a 3 vertex directed graph:
        graph(3, set((1, 2), (2, 1), (1, 3)), True)
        """
        self.vertices = n 
        self.edges = edges 
        self.isDirected = isDirected

    def size(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def is_directed(self):
        return self.isDirected

    def add_edge(self, i, j):
        if i < 0 or i > self.vertices - 1:
            raise Exception("Source vertex out of range")
        elif j < 0 or j > self.vertices - 1:
            raise Exception("Destination vertex out of range")
        elif i == j:
            raise Exception("Self loops forbidden")

        self.edges.add((i, j))

        if not self.isDirected:
            self.edges.add((j, i))

def power_graph(g, directed = False):
    """
    Takes the multiplication table of a magma as
    g:[[int]] and returns its power graph, either
    directed or undirected as determined by the
    directed argument.
    """
    n = len(g)
    Gamma = graph(n, set(()), directed)
    for i in range(n):
        j = g[i][i] 
        while j != i:
            Gamma.add_edge(i, j)
            j = g[i][j]
    return Gamma
