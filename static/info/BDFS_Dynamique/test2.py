import tkinter as tk

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Graph:
    def __init__(self, root):
        self.root = root

    def draw(self):
        def dfs(u, nx, ny, dx, dy):
            nonlocal canvas
            canvas.create_oval(nx - 20, ny - 20, nx + 20, ny + 20, fill="white")
            canvas.create_text(nx, ny, text=str(u.val))
            n = len(u.children)
            if n == 0:
                return
            delta = dx/(n+1)
            for i, v in enumerate(u.children):
                nx2 = nx - dx/2 + delta*(i+1)
                ny2 = ny + dy
                canvas.create_line(nx, ny, nx2, ny2)
                dfs(v, nx2, ny2, dx/2, dy)

        master = tk.Tk()
        master.title("Arbre")
        canvas_width = 500
        canvas_height = 400
        canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
        canvas.pack()

        dfs(self.root, canvas_width/2, 50, 200, 80)

        tk.mainloop()

# Création des noeuds
nodes = [Node(i) for i in range(1, 15)]

# Ajout des enfants aux noeuds
nodes[0].children = [nodes[1], nodes[6], nodes[10]]
nodes[1].children = [nodes[2], nodes[3]]
nodes[6].children = [nodes[7], nodes[8], nodes[9]]
nodes[10].children = [nodes[11]]
nodes[11].children = [nodes[12], nodes[13]]
nodes[3].children = [nodes[4], nodes[5]]

# Création du graphe
graph = Graph(nodes[0])

# Affichage du graphe dans une fenêtre graphique
graph.draw()
