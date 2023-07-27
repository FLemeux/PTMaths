import tkinter as tk
from collections import deque
import time


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.item_id = None
    
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
        self.queue = deque()
        self.visited = set()
        self.queue_items = []

    def update_queue_display(self):
    # Récupérer l'élément en haut de la file
        top_item_id = self.queue_items[0]

    # Mettre à jour la position de tous les sommets dans la file
        for i, item_id in enumerate(self.queue_items):
            x, y = canvas.coords(item_id)
            canvas.coords(item_id, (i + 1) * 50, y)

    # Déplacer l'élément en haut de la file à la bonne position
        x, y = canvas.coords(top_item_id)
        canvas.coords(top_item_id, 10, canvas_height - 50)

        

    def draw(self):
        def bfs(u, nx, ny, dx, dy):
            nonlocal canvas
            u.item_id = canvas.create_oval(nx - 20, ny - 20, nx + 20, ny + 20, fill="white", tags=str(u.val))
            canvas.create_text(nx, ny,text=str(u.val), font=("Arial",20,"bold"))
            n = len(u.children)
            if n == 0:
                return
            delta = dx/(n+1)
            for i, v in enumerate(u.children):
                nx2 = nx - dx/2 + delta*(i+1)
                ny2 = ny + dy
                canvas.create_line(nx, ny, nx2, ny2)
                bfs(v, nx2, ny2, dx/2, dy)

        def bfs_traversal(u):
            self.queue.append(u)

            # Ajouter le premier élément dans la liste queue_items
            item = canvas.create_text(10, canvas_height - 50, text=str(u.val), font=('Arial', 30, 'bold'))
            self.queue_items.append(item)
            offset_x = 0
            item_width = 50
            canvas.itemconfig(u.item_id, fill="gray")
            canvas.update()
            input('')

            while self.queue:
                #input('')
                u = self.queue.popleft()
                self.visited.add(u)
                for v in u.children:
                    if v not in self.visited:
                        input('')
                        self.queue.append(v)


                        
                        

                        # Ajouter le sommet dans la liste queue_items
                        item = canvas.create_text(50 + offset_x * item_width, canvas_height - 50, text=str(v.val), font=('Arial', 30, 'bold'))
                        self.queue_items.append(item)
                        offset_x += 1
                        canvas.itemconfig(v.item_id, fill="gray")
                        canvas.update()

                        # Colorer le nœud visité en gris




                # Colorer le nœud visité en noir
                input('')
                canvas.itemconfig(u.item_id, fill="black")
                

                # Retirer le sommet défilé de la liste queue_items
                item_id = self.queue_items.pop(0)
                canvas.delete(item_id)
                canvas.update()
                
                

        master = tk.Tk()
        master.title("BFS")
        canvas_width = 1000
        canvas_height = 600
        canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
        canvas.pack()

        bfs(self.root, canvas_width/2, 50, 1100, 120)

        bfs_traversal(self.root)
        """
        for i, (node, level) in enumerate(self.root.traverse()):
            node_x = (i + 1) * (canvas_width / (len(level) + 1))


            node_y = (len(level) + 1) * 80
           

            node.item_id = canvas.find_withtag(str(node.val))[0]
            canvas.coords(node.item_id, node_x - 20, node_y - 20, node_x + 20, node_y + 20)
            if node in self.visited:
                canvas.create_oval(node_x - 25, node_y - 25, node_x + 25, node_y + 25, fill="gray", outline="black")
                canvas.create_text(node_x, node_y, text=str(node.val), font=('Arial', 16, 'bold'))
            else:
                canvas.create_oval(node_x - 25, node_y - 25, node_x + 25, node_y + 25, fill="white", outline="black")
                canvas.create_text(node_x, node_y, text=str(node.val))"""
        tk.mainloop()

nodes = [Node(i) for i in range(1, 15)]


nodes[0].children = [nodes[1], nodes[2], nodes[3]]
nodes[1].children = [nodes[4], nodes[5]]
nodes[2].children = [nodes[6], nodes[7], nodes[8]]
nodes[3].children = [nodes[9]]
nodes[5].children = [nodes[10], nodes[11]]
nodes[9].children = [nodes[12], nodes[13]]

# Dessin de l'arbre
graph = Graph(nodes[0])

graph.draw()




