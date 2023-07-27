from collections import deque

def DFS(G,s):
     L=deque([s])
     P={s:None}
     visites={}
     for u in G:
          visites[u]="Blanc"
     visites[s]="Gris"
     while L:
          u=L[-1]
          voisins=[v for v in G[u] if visites[v]=="Blanc"]
          if voisins: #len(voisins)>0
               v=voisins[0]
               L.append(v)
               visites[v]="Gris"
               P[v]=u
          else:
               visites[u]="Noir"
               L.pop()
     return P
          
D={1 : [2,7,11], 2 : [1,3,4], 3 : [2], 4 : [2,5,6], 5 : [4], 6 : [4], 7 : [1,8,9,10], 8 : [7], 9 : [7], 10 : [7], 11 : [1,12], 12 : [11,13,14], 13 : [12], 14 : [12]}
          
