import tkinter as tk
from collections import deque

class PileApp:
    def __init__(self, master):
        self.master = master
        master.title("Pile App")
        
        self.pile = deque()
        self.canvas = tk.Canvas(master, width=200, height=400, bg='white')
        self.canvas.pack(pady=20)
        
        self.button_push = tk.Button(master, text="Empiler", command=self.push)
        self.button_push.pack(side="left", padx=10)
        
        self.button_pop = tk.Button(master, text="Dépiler", command=self.pop)
        self.button_pop.pack(side="right", padx=10)
        
        self.update_canvas()
        
    def push(self):
        element = len(self.pile) + 1
        self.pile.append(element)
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


import tkinter as tk

# définir la fenêtre principale
root = tk.Tk()
root.title("Pile et parcours en profondeur")
root.geometry("800x400")

# définir la pile
pile = []

# fonction pour mettre à jour l'affichage de la pile
def update_pile():
    global pile_text
    pile_text.set("Pile : " + str(pile))

# fonction pour ajouter un élément à la pile
def push():
    global pile_entry
    element = pile_entry.get()
    pile.append(element)
    update_pile()
    pile_entry.delete(0, tk.END)

# fonction pour supprimer le dernier élément de la pile
def pop():
    pile.pop()
    update_pile()

# fonction pour mettre à jour la couleur du sommet
def update_couleur(sommet):
    global canvas
    if sommet["couleur"] == "white":
        sommet["couleur"] = "grey"
    elif sommet["couleur"] == "grey":
        sommet["couleur"] = "black"
    canvas.itemconfigure(sommet["nom"], fill=sommet["couleur"])
    canvas.update()

# fonction pour parcourir en profondeur
def parcours_profondeur(sommet):
    push()
    update_couleur(sommet)
    for voisin in sommet["voisins"]:
        if voisin["couleur"] == "white":
            parcours_profondeur(voisin)
    pop()
    update_couleur(sommet)

# définir les sommets de l'arbre
sommet1 = {"nom": 1, "x": 400, "y": 50, "couleur": "white", "voisins": []}
sommet2 = {"nom": 2, "x": 250, "y": 150, "couleur": "white", "voisins": []}
sommet3 = {"nom": 3, "x": 150, "y": 250, "couleur": "white", "voisins": []}
sommet4 = {"nom": 4, "x": 350, "y": 250, "couleur": "white", "voisins": []}
sommet5 = {"nom": 5, "x": 50, "y": 350, "couleur": "white", "voisins": []}
sommet6 = {"nom": 6, "x": 250, "y": 350, "couleur": "white", "voisins": []}
sommet7 = {"nom": 7, "x": 550, "y": 150, "couleur": "white", "voisins": []}
sommet8 = {"nom": 8, "x": 450, "y": 250, "couleur": "white", "voisins": []}
sommet9 = {"nom": 9, "x": 550, "y": 250, "couleur": "white", "voisins": []}
sommet10 = {"nom": 10, "x": 650, "y": 250, "couleur": "white", "voisins": []}
sommet11 = {"nom": 11, "x": 400, "y": 150, "couleur": "white", "voisins": [12]}
sommet12 = {"nom": 12, "x": 450, "y": 200, "couleur": "white", "voisins": [13, 14]}
sommet13 = {"nom": 13, "x": 500, "y": 250, "couleur": "white", "voisins": []}
sommet14 = {"nom": 14, "x": 550, "y": 350, "couleur": "white", "voisins": []}

# Ajouter les sommets dans une liste pour faciliter la boucle
sommets = [sommet1, sommet2, sommet3, sommet4, sommet5, sommet6, sommet7, sommet8, sommet9, sommet10, sommet11, sommet12, sommet13, sommet14]

# Définir la fonction pour dessiner les sommets
def dessiner_sommet(sommet):
    if sommet["couleur"] == "white":
        couleur = "white"
    elif sommet["couleur"] == "gray":
        couleur = "gray"
    else:
        couleur = "black"
    canvas.create_oval(sommet["x"]-25, sommet["y"]-25, sommet["x"]+25, sommet["y"]+25, fill=couleur)
    canvas.create_text(sommet["x"], sommet["y"], text=str(sommet["nom"]))

# Définir la fonction pour dessiner les arêtes
def dessiner_arete(sommet1, sommet2):
    canvas.create_line(sommet1["x"], sommet1["y"], sommet2["x"], sommet2["y"])

# Définir la fonction pour dessiner le graphe complet
def dessiner_graphe():
    for sommet in sommets:
        dessiner_sommet(sommet)
        for voisin_nom in sommet["voisins"]:
            voisin = next((s for s in sommets if s["nom"] == voisin_nom), None)
            dessiner_arete(sommet, voisin)

# Définir la fonction pour mettre à jour la couleur d'un sommet
def update_couleur(sommet_courant):
    """
    Met à jour la couleur du sommet courant en fonction de son état
    """
    if sommet_courant["couleur"] == "blanc":
        sommet_courant["couleur"] = "gris"
    elif sommet_courant["couleur"] == "gris":
        sommet_courant["couleur"] = "noir"
    cercle = canvas.itemconfig(sommet_courant["cercle"], fill=sommet_courant["couleur"])


def parcours_profondeur(sommet_depart):
    """
    Parcours en profondeur de l'arbre à partir du sommet de départ
    """
    pile = [sommet_depart]
    while len(pile) > 0:
        sommet_courant = pile[-1]
        update_couleur(sommet_courant)
        canvas.update()
        time.sleep(1)
        if "enfants" in sommet_courant:
            for enfant in sommet_courant["enfants"]:
                if enfant["couleur"] == "blanc":
                    pile.append(enfant)
        else:
            pile.pop()

# Exemple d'utilisation
parcours_profondeur(sommet1)

