import sys
import networkx as nx 
import matplotlib.pyplot as plt
from math import inf 
from heapq import heapify,heappop,heappush 
def dijkstra(graph, source):

    unvisited = set(graph.keys())
    distances = {vertex: sys.maxsize for vertex in unvisited}
    distances[source] = 0
    predecessor = {vertex: None for vertex in unvisited}

    while unvisited:
        current = min(unvisited, key =lambda vertex: distances[vertex])
        unvisited.remove(current)
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current

    return distances, predecessor


def draw_graph(graph):
    G = nx.DiGraph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor, weight=graph[node][neighbor])

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=6)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family = 'sans-serif')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

graph ={
    'a': {'b': 3, 'c':4,'d':7},
    'b': {'c':1, 'f':5},
    'c': {'f':6, 'd':2},
    'd': {'e':3, 'g':6},
    'e': {'g':3,'h':4},
    'f': {'e': 1, 'h':8},
    'g': {'h': 2},
    'h': {'g': 2}
}
draw_graph(graph)
distances, predecessor = dijkstra(graph,'a')
print (distances)
print (find_path(graph, 'a','h'))




