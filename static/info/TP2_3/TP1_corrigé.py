from collections import deque
import numpy as np

######################
######################
######################
# 2 exemples pour la suite
# Un graphe avec cycle
D={}
D[1]=[2,4,6]
D[2]=[1,3]
D[3]=[2,5]
D[4]=[1,6]
D[5]=[3,7]
D[6]=[1,4]
D[7]=[5]

# Un deuxième sans cycle

E={}
E[1]=[2,4]
E[2]=[1,3]
E[3]=[2,5]
E[4]=[1,6]
E[5]=[3,7]
E[6]=[4]
E[7]=[5]
######################
######################
######################


######################
# Exercice 2 : degré, nombre de voisins
######################
def degre(G,s):
     return len(G[s])
######################
######################




######################
# Exercice 3 : dictionnaire v.s. matrice d'adjacence
######################

# Dictionnaire->Matrice
def matrice(D):
     n=len(D)
     G=np.zeros((n,n))
     for i in range(n):
          for j in range(n):
               if j in D[i]:
                    G[i,j]=1
               else:
                    G[i,j]=0
     return G

# Matrice->dictionnaire
def dico(M):
     n=len(M)# ou np.shape(M)[0]
     D={}
     for i in range(n):
          D[i]=[j for j in range(n) if M[i,j]==1]
     return D
######################
######################


# Exercice 4 : Tri par comptage
def comptage(L):
     D={}
     for x in L:
          D[x]=0
     for x in L:
          D[x]+=1
     return D

def TriComptage(L):
     D=comptage(L)
     L_tri=[] #  liste L triée
     M=max(D) # on peut aussi écrire une boucle pour déterminer le max
     for i in range(M+1) : # les éléments de la liste sont parmi les entiers compris entre 0 et M...
          if i in D:
               L_tri=L_tri+D[i]*[i] # on ajoute D[i] fois l'entier i (s'il est dans le dictionnaire et donc dans la liste L)
     return L_tri
          


######################
# Exercice 5
# Parcours en largeur
######################
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
######################
######################



######################
# Exercice 6 : connexité
######################
def connexe(G):
     Test=True
     for v in G:
          if len(BFS(G,v))!=len(G):
               Test=False
     return Test # Remarque : le fait de parcourir tous les sommets n'est pas utile

def connexe2(G):
     s=list(G)[0]
     return len(BFS(G,s))==len(G)

G1={} # 2 composantes connexes
G1[1]=[2]
G1[2]=[1]
G1[3]=[4]
G1[4]=[3]

G2={} # 1 seule
G2[1]=[2,3,4]
G2[2]=[1,3,4]
G2[3]=[1,2,4]
G2[4]=[1,2,3]

def composantes_connexes(G):
     L=[]
     G1=dict(G)
     if len(G)==0:
          return {}
     else:
          while len(G1)>0:
               u=list(G1)[0] # ou list(BFS(G1,u).keys())
               vu=BFS(G1,u)#u et les sommets sur un chemin partant de u
               L.append(list(vu.keys()))
               for x in vu.keys():
                    G1.pop(x)
     return L

# remarque : comment obtenir le nombre de composantes connexes ? ->len(composantes_connexes(G))

######################
######################



######################
#Exercice 7
######################
def cycle_BFS(G,s):
    couleurs={} # sommets visités
    for v in G.keys():
        couleurs[v]="blanc"
    L=deque([s])#file des sommets
    parents={s : None}#pas de prédécesseurs pour le sommet de départ
    while L:
        u=L.popleft() # on défile dans u
        couleurs[u]="Noir" # on dit que courant est visité
        for v in G[u]: # on découvre les voisins de courant
            if couleurs[v]=="blanc":
                L.append(v)
                couleurs[v]="gris"
                parents[v]=u
            elif couleurs[v]=="gris":
                 # on tombe sur un voisin gris (déjà rencontré mais pas via le sommet u) : on a détecté un cycle
                return True
    return False

# Pour tester :
G3={}
G3["a"]=["b","c"]
G3["b"]=["a","d","e"]
G3["c"]=["a","d"]
G3["d"]=["b","c","e"]
G3["e"]=["b","d","f","g"]
G3["f"]=["e","g"]
G3["g"]=["e","f","h"]
G3["h"]=["g"]

# Remarques : si plusieurs composantes connexes : on peut écrire

#for c in composantes_connexes(G1):cycle_BFS(G1,list(c)[0])

######################
######################



######################
# Exercice 8
######################
# Parcours en profondeur
def DFS(G,s):
     P={}
     L=deque([])
     couleurs={}
     P[s]=None
     for u in G:
          couleurs[u]="blanc"
     couleurs[s]="gris"
     L.append(s)
     while L:
          u=L[-1]
          R=[v for v in G[u] if couleurs[v]=="blanc"] # création d'une liste en compréhension. Sinon on remplit R avec une boucle for
          if R:
               v=R[0]
               L.append(v)
               P[v]=u
               couleurs[v]="gris"
          else:
               L.pop()
               couleurs[u]="noir"
     return P



######################
# Exercice 9
######################
def chemin(G,s1,s2):
     return s2 in DFS(G,s1)

# Construction d'un chemin

def chemin1(G,s1,s2):
     if s2 not in DFS(G,s1):
          return None # ou False
     else:
          P=DFS(G,s1)
          chemin=[]
          courant=s2 # sommet courant
          while courant!=s1:
               print(courant)
               chemin.append(courant)
               courant=P[courant] # on remplace par son prédécesseur
          chemin.append(s1)
          return chemin
          
######################




######################
# Exercice 10
######################
def biparti(G):
     visites={}
     couleurs={}
     dep=list(G)[0]
     for u in G:
          visites[u]="Blanc"
     L=deque([dep])#Pile contenant le premier sommet
     P={dep : None}#les prédécesseurs de u, vide pour le sommet de départ
     visites[dep]="Gris"
     couleurs[dep]="Rouge"
     while L: # L non vide
          u=L[-1]#on plance sans dépiler le sommet de L dans u
          R=[v for v in G[u] if visites[v]=="Blanc"]
          if R: # R non vide
               v=R[0] # arbitraire (le dernier convient aussi)
               P[v]=u
               visites[v]="Gris"
               L.append(v)
               if couleurs[u]=="Rouge":
                    couleurs[v]="Bleu"
               else:
                    couleurs[v]="Rouge"
          else:
               L.pop()
               visites[u]="Noir"
     Test=True
     for u in G:
          for v in G[u]:
               if couleurs[u]==couleurs[v]: # si un voisin de u est de la même couleur que u lors du parcours en profondeur, le graphe n'est pas biparti.
                    Test=False
     return Test

M={}
M[1]=[2,4,6]
M[2]=[1,3,5]
M[3]=[2,4,6]
M[4]=[1,3,5]
M[5]=[2,4,6]
M[6]=[1,3,5]



######################
# Exercice 11
######################
def rec(G, courant,P) :
        for v in G[courant] :
            if v not in P :
                P[v]=courant
                rec(G, v,P)

def DFS_rec(G, dep) :
    P={dep:None}
    rec(G, dep,P)
    return P

# Exercice 12: cycle + chemin avec DFS

def cycle_DFS(G,sommet):
    chemin=[]
    visite={} # sommets visités
    for v in G:
        visite[v]="blanc"
    #dep=list(G)[0]#sommet de départ
    L=deque([sommet])#file des sommets
    P={sommet : None}#pas de prédécesseurs pour le sommet de départ
    while L:
        courant=L.pop() # on défile dans courant
        if visite[courant]=="blanc":
            visite[courant]="noir"
            # on dit que courant est visité lorsqu'il est défilé
            for v in G[courant]: # on découvre les voisins de courant
                print(courant,v)
                if visite[v]=="blanc":
                    if v not in P:
                        L.append(v)
                        print(L)
                        P[v]=courant
                    else:
                        ancien_parent=P[v]
                        chemin.append(courant)
                        chemin.append(v)
                        chemin.append(ancien_parent)
                        while courant!=ancien_parent:
                            parent=P[courant]
                            courant=parent
                        return chemin
    return False

G={}
G[1]=[2,4,6]
G[2]=[1,3]
G[3]=[2,5]
G[4]=[1,6]
G[5]=[3,7]
G[6]=[1,4]
G[7]=[5]

