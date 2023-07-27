import tkinter as tk
import time


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    def traverse(self):
        nodes = [(self, [1])]
        while nodes:
            node, level = nodes.pop(0)
            yield node, level
            if len(node.children) == 0:
                continue
            for i, child in enumerate(node.children):
                child_level = level + [i+1]
                nodes.append((child, child_level))


class Graph:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.visited = set()

    def draw(self):
        def dfs(u, nx, ny, dx, dy):
            nonlocal canvas
            u.item_id = canvas.create_oval(nx - 20, ny - 20, nx + 20, ny + 20, fill="white", tags=str(u.val))
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

        def dfs_traversal(u):
            self.stack.append(u)
            self.visited.add(u)
            canvas.itemconfig(u.item_id, fill="gray")
            canvas.update()
            time.sleep(1)
            for v in u.children:
                if v not in self.visited:
                    dfs_traversal(v)
            self.stack.pop()
            canvas.itemconfig(u.item_id, fill="black")
            canvas.update()

        master = tk.Tk()
        master.title("Arbre")
        canvas_width = 800
        canvas_height = 600
        canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
        canvas.pack()

        dfs(self.root, canvas_width/2, 50, 400, 120)

        dfs_traversal(self.root)
        for i, (node, level) in enumerate(self.root.traverse()):
            node_x = (i + 1) * (canvas_width / (len(level) + 1))
            node_y = len(level) * 80 + 100
            node.item_id = canvas.find_withtag(str(node.val))[0]
            canvas.coords(node.item_id, node_x - 20, node_y - 20, node_x + 20, node_y + 20)

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

# Dessin de l'arbre
graph = Graph(nodes[0])
graph.draw()
