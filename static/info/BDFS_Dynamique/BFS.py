from collections import deque

#Exercice 6 : connexité

#On rappelle le fonction BFS

def BFS(G,s):
     L=deque([s])
     P={s : None}
     visites={}
     for u in G:
          visites[u]="Blanc"
     # On peut écrire visites[s]="Gris"
     while L:
          u=L.popleft()
          visites[u]="Noir"
          voisins_blancs=[v for v in G[u] if visites[v]=="Blanc"]
          for v in voisins_blancs:
               visites[v]="Gris"
               P[v]=u
               L.append(v)
     return P

D={1 : [2,3,4], 2 : [1,5,6], 3 : [1,7,8,9], 4 : [1,10], 5 : [2], 6 : [2,11,12], 7 : [3], 8 : [3], 9 : [3], 10 : [4, 13, 14], 11 : [6], 12 : [6], 13 : [10], 14 : [10]}
P=BFS(D,1)

D1={"A" : ["B"], "B":["A"], "D":["E","C"], "E":["D","C"], "C":["D","E"]}

#Q1
#Un graphe est connexe si et seulement si BFS(G,s) est de longueur len(G) pour toute sommet s

#Q2
def connexe(G):
     T=True
     for v in G:
          if len(BFS(G,v))<len(G):
               T=False
     return T

#Q3

def composantes(G):
     L=[]
     while G:
          s=list(G)[0]
          Comp=[]
          for v in BFS(G,s):
               Comp.append(v)
               G.pop(v)
          L=L+[Comp]
     return L

def BFS_cycle(G,s):
     L=deque([s])
     P={s : None}
     visites={}
     for u in G:
          visites[u]="Blanc"
     while L:
          u=L.popleft()
          visites[u]="Noir"
          voisins=[v for v in G[u] if visites[v]!="Noir"]
          for v in voisins:
               if visites[v]=="Blanc":
                    visites[v]="Gris"
                    P[v]=u
                    L.append(v)
               elif visites[v]=="Gris":
                    return True
     return P,False




