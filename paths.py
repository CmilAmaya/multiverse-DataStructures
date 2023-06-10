from graph import DirectedGraph, build_graph

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
