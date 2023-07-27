from tkinter import *
from tkinter import messagebox
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for i in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def dfs(self, start):
        visited = [False] * self.vertices
        stack = [start]
        visited[start] = True

        while stack:
            current_vertex = stack.pop()
            print(current_vertex)
            self.draw_visited_node(current_vertex)
            for i in range(self.vertices):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    stack.append(i)
                    visited[i] = True
            self.draw_stack(stack)

    def draw_visited_node(self, node):
        # Code pour dessiner un nœud visité dans la fenêtre graphique
        pass

    def draw_stack(self, stack):
        # Code pour afficher la pile d'exécution dans la fenêtre graphique
        pass

# Code pour initialiser la fenêtre graphique
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Code pour initialiser le graphe et ajouter des arêtes
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Code pour lancer le parcours en profondeur
graph.dfs(0)

# Code pour lancer la boucle principale de la fenêtre graphique
root.mainloop()
