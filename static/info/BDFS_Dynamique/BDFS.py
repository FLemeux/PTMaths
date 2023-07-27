from collections import deque
def BFS(G,s):
     P={s : None}
     visites={}
     for u in G:
          visites[u]="Blanc"
     L=deque([s])
     visites[s]="Gris"
     while L:
          u=L.popleft()
          visites[u]="Noir"
          voisins_blancs=[v for v in G[u] if visites[v]=="Blanc"]
          for v in voisins_blancs:
               P[v]=u
               visites[v]="Gris"
               L.append(v)
     return P

G={1 : [2,3,4], 2 : [1,5,6], 3 : [1,7,8,9], 4 : [1,10], 5 : [2], 6 : [2,11,12], 7 : [3], 8 : [3], 9 : [3], 10 : [4, 13, 14], 11 : [6], 12 : [6], 13 : [10], 14 : [10]}


def DFS(G,s):
     P={s : None}
     visites={}
     for u in G:
          visites[u]="Blanc"
     L=deque([s])
     visites[s]="Gris"
     while L:
          u=L[-1]
          voisins_blancs=[v for v in G[u] if visites[v]=="Blanc"]
          if voisins_blancs:
               for v in voisins_blancs:
                    L.append(v)
                    P[v]=u
                    visites[v]="Gris"
          else:
               visites[u]="Noir"
               L.pop()
     return P
     

H={1 : [2,7,11], 2 : [1,3,4], 3 : [2], 4 : [2,5,6], 5 : [4], 6 : [4], 7 : [1,8,9,10], 8 : [7], 9 : [7], 10 : [7], 11 : [1,12], 12 : [11,13,14], 13 : [12], 14 : [12]}


