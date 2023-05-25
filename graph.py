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
    
    def find_paths(self, current, node_obj_f, paths = []):
        if(current.get_name() != node_obj_f.get_name() and self.graph_dict[current]):
            paths.append([current.get_name(), self.graph_dict[current][0].get_name()])
            current = self.graph_dict[current][0]
            self.find_paths(current, node_obj_f, paths)
        elif(not self.graph_dict[current]):
            return False , paths
        return True, paths
    
    def add_new_node(self, Graph):
        g = Graph() 

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


def build_graph(Graph):
    g = Graph()
    nodos_str = [str(x) for x in range(1,5)]
    vertex_names = []
    

    for v in nodos_str:
        g.add_vertex(Vertex(v))
        vertex_names.append(v)

    random.shuffle(nodos_str)
    for i in range(len(nodos_str) - 1):
        g.add_edge(Edge(g.get_vertex(nodos_str[i]), g.get_vertex(nodos_str[i + 1])))
        
    print(vertex_names)
    return g, vertex_names

G1, vertex_names = build_graph(DirectedGraph)
print(f"Grafo:\n{G1}")

# Esto no agrega nodos, por favor espere en la fila :3
nd_inicial = input("Ingrese el nodo inicial: ")
nd_final = input("Ingrese el nodo final: ")

# Validar que exista el nodo en el grafo
node_obj_i = G1.get_vertex(str(nd_inicial))
node_obj_f = G1.get_vertex(str(nd_final))

sucess, paths = G1.find_paths(node_obj_i, node_obj_f)

if (not sucess):
    print("error, justo se le dio por encontrar el primero y el ultimo nodo")
else:
    print(f"La ruta para ir del nodo {nd_inicial} al nodo {nd_final} es {paths}")

def add_new_node(nuevo_nodo = input("Nodo a agregar:")):
    nodo_final = 0
    for k,v in G1.graph_dict.items():
        node_list = [node.get_name() for node in v]
        if node_list == []:
            nodo_final = k.get_name()
            str(nodo_final)
    G1.add_vertex(Vertex(nuevo_nodo))
    G1.add_edge(Edge(G1.get_vertex(str(nodo_final)),G1.get_vertex(str(nuevo_nodo))))
    return f"Nodo {nuevo_nodo} agregado a:\n{G1}"

print(add_new_node())





