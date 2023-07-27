from collections import deque

def BFS(G,s):
     P={}
     L=deque([])
     couleurs={}
     for u in G:
          couleurs[u]="blanc"
     couleurs[s]="gris"
     L.append(s)
     P[s]=None
     while L:
          u=L.popleft()
          couleurs[u]="noir"
          for v in G[u]:
               if couleurs[v]=="blanc":
                    L.append(v)
                    P[v]=u
                    couleurs[v]="gris"
     return P

D={"A":["B"], "B":["A"], "C":["D","E"],"D":["C","E"],"E":["C","D"]}

D1={"A":["B","D"], "B":["A"], "C":["D","E"],"D":["C","E","A"],"E":["C","D"]}

def connexe(G):
     for v in G:
          if len(BFS(G,v))<len(G):
               return False
     return True

def connexe1(G):
     return len(BFS(G,list(G)[0]))==len(G)

def composantes(G):
     L=[] # contiendra la liste des composantes connexes
     while G: # non vide
          u=list(G)[0] # permet d'accéder à l'une des clés de G (un sommet)
          Lu=[] # liste des éléments appartenant à la même composante connexe
          for x in BFS(G,u): # on parcourt tous les sommets accéssible à partir de u
               G.pop(x) # on les supprime du dictionnaire
               Lu.append(x) # on l'ajoute dans la composante connexe de u
          L.append(Lu) # une nouvelle composante connexe ajoutée à L
     return L
     
# Ex7, Ex3, Ex4, Ex 9
# Ex 11, Ex12, Ex10
               
               







     
