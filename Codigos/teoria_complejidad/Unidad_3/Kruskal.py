#=======================
#Dante Alegria Romero
#25/05/2024
#Algoritmo de Kruskal
#=======================

import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Creamos el grafo
G = nx.Graph()

# Añadimos los nodos
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Añadimos las aristas
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=1)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=3)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'D', weight=1)

#Funcion para verificar nuestros resultados
def Verificacion():
    T = nx.minimum_spanning_tree(G)
    print("Aristas del arbol de expansion minima: ", T.edges(data=True))
    print("Peso del arbol de expansion minima: ", T.size(weight='weight'))

def Kruskal():
    T = nx.Graph()
    aristas = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    for nodo in G.nodes():
        T.add_node(nodo)
    for arista in aristas:
        if nx.has_path(T, arista[0], arista[1]) == False:
            T.add_edge(arista[0], arista[1], weight=arista[2]['weight'])
    print("Aristas del arbol de expansion minima: ", T.edges(data=True))
    print("Peso del arbol de expansion minima: ", T.size(weight='weight'))

def kruskal_recursive(edges, uf, mst_edges, index=0):
    if len(mst_edges) == len(uf.parent) - 1 or index == len(edges):
        return mst_edges

    u, v, weight = edges[index]

    if uf.find(u) != uf.find(v):
        uf.union(u, v)
        mst_edges.append((u, v, weight))

    return kruskal_recursive(edges, uf, mst_edges, index + 1)

def Kruskal_recursivo():
    edges = sorted(G.edges(data=True), key=lambda edge: edge[2]['weight'])
    edges = [(u, v, data['weight']) for u, v, data in edges]
    uf = UnionFind(G.nodes)
    mst_edges = kruskal_recursive(edges, uf, [])

    T = nx.Graph()
    for u, v, weight in mst_edges:
        T.add_edge(u, v, weight=weight)

    print("Aristas del arbol de expansion minima (recursivo): ", T.edges(data=True))
    print("Peso del arbol de expansion minima (recursivo): ", T.size(weight='weight'))


def main():
    print('Funcion de Verificacion:')
    Verificacion()
    print('Version Iterativa:')
    Kruskal()
    print('Version Recursiva:')
    Kruskal_recursivo()

if __name__ == '__main__':
    main()
