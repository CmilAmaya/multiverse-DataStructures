import random
 
class DirectedGraph:
    def __init__(self):
        self.graph_dict = {}
        self.first_node = None
        self.last_node = None

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = []
    
    def insert_vertex(self):
        vertex_name = input("Nodo a agregar:")
        self.add_vertex(Vertex(vertex_name))
        self.add_edge(Edge(self.last_node,self.get_vertex(str(vertex_name))))
        return G1

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
        if(current.get_name() == self.last_node.get_name() or 
           node_obj_f.get_name() == self.first_node.get_name()):
            return False , paths
        if(current.get_name() != node_obj_f.get_name() and 
           self.graph_dict[current] and 
           self.graph_dict[current][0].get_name() != self.last_node.get_name()):
            paths.append([current.get_name(), self.graph_dict[current][0].get_name()])
            current = self.graph_dict[current][0]
            self.find_paths(current, node_obj_f, paths)
        elif(not self.graph_dict[current] or current.get_name() == self.first_node.get_name()):
            return False , paths
        return True, paths
    
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
    vertex_names = []
    nodos_str = []
    for x in range(1,36):
        nodos_str.append(str(x))
        g.add_vertex(Vertex(str(x)))
        
    random.shuffle(nodos_str)
    for i in range(len(nodos_str) - 1):
        vertex_names.append(nodos_str[i])
        vertex_names.append(nodos_str[i + 1])

        if i == 0:
            g.first_node = g.get_vertex(nodos_str[i])

        if i == (len(nodos_str) - 2):
            g.last_node = g.get_vertex(nodos_str[i + 1])

        g.add_edge(Edge(g.get_vertex(nodos_str[i]), g.get_vertex(nodos_str[i + 1])))

    return g, vertex_names 

G1, names = build_graph(DirectedGraph)
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

print(G1.insert_vertex())
diccionario = G1.graph_dict
print("Nombre de los nodos:", names)
final_names = []
for elemento in names:
    if elemento not in final_names:
        final_names.append(elemento)
print("Lista sin repetidos:", final_names)
"""for elemento in final_names: 
    print("Cada elemento:", elemento)"""