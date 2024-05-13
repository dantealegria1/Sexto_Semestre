#========================================
# Problema:     Agente Viajero
# Algoritmo:    Fuerza Bruta
# Fecha:        11/05/24
#========================================

#Librerias Necesarias
import networkx as nx
import matplotlib.pyplot as plt
import math
import random

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos (puntos en Aguascalientes)
G.add_node("Centro de Distribucion", pos=(21.797002915870696, -102.28046633923687))
G.add_node("Casa 1", pos=(21.85490001683624, -102.26504374226292))
G.add_node("Casa 2", pos=(21.853740600742764, -102.34306832781398))
G.add_node("Casa 3", pos=(21.90351643596852, -102.24558201609902))
G.add_node("Casa 4", pos=(21.90638253550554, -102.28153665890189))
G.add_node("Casa 5", pos=(21.9380714883858, -102.25934916251998))
G.add_node("Casa 6", pos=(21.928195119225208, -102.28013241671694))
G.add_node("Casa 7", pos=(21.886794591014723, -102.28449322733664))

#Funcion para calcular la distancia eucleriana
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Funcion para agregar las distancias al grafo
def Distances():
    for node1 in G.nodes:
        x1, y1 = G.nodes[node1]['pos']
        for node2 in G.nodes:
            x2, y2 = G.nodes[node2]['pos']
            if node1 != node2:
                G.add_edge(node1, node2, weight=euclidean_distance(x1, y1, x2, y2))

#Algoritmo de fuerza bruta
def Brute_Force():
    nodos = list(G.nodes)[1:]
    Total_Cities = len(nodos)+1
    shortest_path_length = float('inf')
    shortest_path = []
    iterations = math.factorial(Total_Cities)
    for _ in range(iterations):
        random.shuffle(nodos)
        path = ["Centro de Distribucion"] + nodos + ["Centro de Distribucion"] 
        path_length = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
        if path_length < shortest_path_length:
            shortest_path_length = path_length
            shortest_path = path
    return shortest_path, shortest_path_length

#Imprimir el grafo con el camino mas corto
def Print_Solution(shortest_path):
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue')
    shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, width=2, edge_color='red')
    plt.title("Recorrido más corto")
    plt.show()

#Funcion main
def main_Brute():
    Distances()
    shortest_path, shortest_path_length = Brute_Force()
    print("Camino más corto encontrado:", shortest_path)
    print("Distancia del camino más corto:", shortest_path_length)
    Print_Solution(shortest_path)

if __name__ == "__main__":
    main_Brute()
