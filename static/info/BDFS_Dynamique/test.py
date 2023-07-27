import tkinter as tk
from collections import deque

class PileApp:
    def __init__(self, master):
        self.master = master
        master.title("Pile App")
        
        self.pile = deque()
        self.next_element = 1
        self.canvas = tk.Canvas(master, width=200, height=400, bg='white')
        self.canvas.pack(pady=20)
        
        self.button_push = tk.Button(master, text="Empiler", command=self.push)
        self.button_push.pack(side="left", padx=10)
        
        self.button_pop = tk.Button(master, text="Dépiler", command=self.pop)
        self.button_pop.pack(side="right", padx=10)
        
        self.update_canvas()
        
    def push(self):
        self.pile.append(self.next_element)
        self.next_element += 1
        self.update_canvas()
        
    def pop(self):
        if len(self.pile) == 0:
            return
        self.pile.pop()
        self.update_canvas()
        
    def update_canvas(self):
        self.canvas.delete("all")
        y = 400
        for i in self.pile:
            self.canvas.create_oval(50, y, 150, y-50, fill="lightblue")
            self.canvas.create_text(100, y-25, text=str(i), font=("Arial", 20))
            y -= 60
        
        if len(self.pile) == 0:
            self.canvas.create_text(100, 200, text="La pile est vide", font=("Arial", 16))
        
root = tk.Tk()
app = PileApp(root)
root.mainloop()
