import random 
class DirectedGraph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        self.graph_dict[v1].append(v2)

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if v.get_name() == vertex_name:
                return v
        return None

    def __str__(self):
        all_edges = ""
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + "----->" + v2.get_name() + "\n"
        return all_edges


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def __str__(self):
        return self.v1.get_name() + "----->" + self.v2.get_name()


class Vertex:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


def build_graph(Graph):
    g = Graph()
    nodos = ["Pentos", "Winterfell", "Casterly Rock", "Highgarden", "Aguas dulces", "Teusaquillo"]
    for v in nodos:
        g.add_vertex(Vertex(v))
    x = random.choice(nodos)
    if x in nodos: 
        nodos.remove(x)
    y = random.choice(nodos)
    g.add_edge(Edge(g.get_vertex(x), g.get_vertex(y)))
    return g


G1 = build_graph(DirectedGraph)
print(G1)
