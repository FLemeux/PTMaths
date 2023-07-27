from collections import deque

def DFS(G,s):
     L=deque([s])
     P={s : None}
     visites={}
     for u in G:
          visites[u]="Blanc"
     visites[s]="Gris"
     while L: # non vide
          u=L[-1]
          R=[v for v in G[u] if visites[v]=="Blanc"] # R=voisins_blancs
          if R: # non vide
               v=R[0] # par exemple
               P[v]=u
               L.append(v)
               visites[v]="Gris"
          else:
               L.pop()
               visites[u]="Noir"
     return P

D={1 : [2,7,11], 2 : [1,3,4], 3 : [2], 4 : [2,5,6], 5 : [4], 6 : [4], 7 : [1,8,9,10], 8 : [7], 9 : [7], 10 : [7], 11 : [1,12], 12 : [11,13,14], 13 : [12], 14 : [12]}

P=DFS(D,1)
