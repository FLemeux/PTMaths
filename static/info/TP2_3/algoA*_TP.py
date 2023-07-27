##################
##FILES DE PRIORITE
##################

import matplotlib.pyplot as plt

def filePrio():
     return []

def empty(file):
     return file==[]

def put(element,priorite,file):
     for i in range(len(file)):
          e,l=file[i]
          if priorite>l:
               return file[:i]+[(element,priorite)]+file[i:]
     return file+[(element,priorite)]

def delete(file,element):
     for i in range(len(file)):
          if file[i][0]==element:
               return file[0:i]+file[i+1:len(file)]
     return file

def get(file):
     return file.pop()

###############
## GRAPHE CARRE
###############
def carre(n):
     Abs=[]
     Ord=[]
     for i in range(1,n+1):
          for j in range(1,n+1):
               Abs.append(i)
               Ord.append(j)
     return plt.plot(Abs,Ord,"k.")
     
               

def dico_voisins(n):# avec les distances euclidiennes
     V={}
     for i in range(2,n):
          for j in range(2,n):
               V[(i,j)]=[[(i+1,j),1],[(i-1,j),1],[(i,j+1),1],[(i,j-1),1],[(i-1,j+1),2**0.5],[(i+1,j+1),2**0.5],[(i-1,j-1),2**0.5],[(i+1,j-1),2**0.5]]
     for i in range(2,n):
          V[(i,1)]=[[(i-1,1),1],[(i,2),1],[(i+1,1),1],[(i-1,2),2**0.5],[(i+1,2),2**0.5]]
     for i in range(2,n):
          V[(i,n)]=[[(i-1,n),1],[(i,n-1),1],[(i+1,n),1],[(i-1,n-1),2**0.5],[(i+1,n-1),2**0.5]]
     for j in range(2,n):
          V[(1,j)]=[[(1,j-1),1],[(2,j),1],[(1,j+1),1],[(2,j+1),2**0.5],[(2,j-1),2**0.5]]
     for j in range(2,n):
          V[(n,j)]=[[(n,j-1),1],[(n-1,j),1],[(n,j+1),1],[(n-1,j-1),2**0.5],[(n-1,j+1),2**0.5]]
     V[(1,1)]=[[(1,2),1],[(2,1),1],[(2,2),2**0.5]]
     V[(n,1)]=[[(n-1,1),1],[(n,2),1],[(n-1,2),2**0.5]]
     V[(n,n)]=[[(n-1,n),1],[(n,n-1),1],[(n-1,n-1),2**0.5]]
     V[(1,n)]=[[(2,n),1],[(1,n-1),1],[(2,n-2),2**0.5]]
     return V

def dico_voisins2(n):# avec les distances = 1
     V={}
     for i in range(2,n):
          for j in range(2,n):
               V[(i,j)]=[[(i+1,j),1],[(i-1,j),1],[(i,j+1),1],[(i,j-1),1],[(i-1,j+1),1],[(i+1,j+1),1],[(i-1,j-1),1],[(i+1,j-1),1]]
     for i in range(2,n):
          V[(i,1)]=[[(i-1,1),1],[(i,2),1],[(i+1,1),1],[(i-1,2),1],[(i+1,2),1]]
     for i in range(2,n):
          V[(i,n)]=[[(i-1,n),1],[(i,n-1),1],[(i+1,n),1],[(i-1,n-1),1],[(i+1,n-1),1]]
     for j in range(2,n):
          V[(1,j)]=[[(1,j-1),1],[(2,j),1],[(1,j+1),1],[(2,j+1),1],[(2,j-1),1]]
     for j in range(2,n):
          V[(n,j)]=[[(n,j-1),1],[(n-1,j),1],[(n,j+1),1],[(n-1,j-1),1],[(n-1,j+1),1]]
     V[(1,1)]=[[(1,2),1],[(2,1),1],[(2,2),1]]
     V[(n,1)]=[[(n-1,1),1],[(n,2),1],[(n-1,2),1]]
     V[(n,n)]=[[(n-1,n),1],[(n,n-1),1],[(n-1,n-1),1]]
     V[(1,n)]=[[(2,n),1],[(1,n-1),1],[(2,n-2),1]]
     return V

################
# DIJKSTRA CARRE
################

def DIJKSTRA_carre(n,dep,fin): # dans le tp
     G=dico_voisins(n)
     file=filePrio()
     file=put(dep,0,file)
     distances_origines={dep:0}
     for v in G:
          if v!=dep:
               distances_origines[v]=float("inf")
     parents={dep:None}
     chemin=[]
     plt.pause(0.1)
     carre(n)
     plt.plot(dep[0],dep[1],'bo')
     plt.plot(fin[0],fin[1],'bo')
     plt.pause(0.1)
     input()
     while not empty(file):
          s,d=get(file) # sommet et distance au parent
          if s!=fin:
               for v,delta in G[s]:
                    distance=distances_origines[s]+delta
                    if distance<distances_origines[v]:
                         distances_origines[v]=distance
                         file=put(v,distance,file)
                         parents[v]=s
                         plt.plot(v[0],v[1],"ro")
                         plt.pause(0.1)
          else:
               plt.plot(s[0],s[1],'bo')
               chemin=[fin]
               while s!=dep:
                    s=parents[s]
                    chemin=[s]+chemin
                    plt.plot(s[0],s[1],'bo')
                    plt.pause(0.1)
     return distances_origines[fin],chemin

def euclide(A,B):
     return ((A[1]-B[1])**2+(A[0]-B[0])**2)**0.5

# avec Dijkstra : à chaque déplacement, on cherche le sommet le plus proche
# c'est-à-dire le plus proche de l'origine

# Avec AlgoA* on fait de même mais on stocke dans la file de priorité pas uniquement
# la distance_origine mais la distance_origine+distance_fin

####################
# ALGO A* dans un carré
####################
def algoA(n,dep,fin):
     visité={}
     G=dico_voisins(n)
     #A) distances à l'origine
     distances_origines={}
     distances_origine={dep:0}
     for v in G:
          if v!=dep:
               distances_origine[v]=float("inf")
     #B) heuristique : distance (euclidienne=vol oiseau) à la fin
     h={} # heuristique
     for v in G:
          h[v]=euclide(v,fin)
     #C) score=distance_origine+distance_fin
     score={}
     score[dep]=h[dep]+distances_origine[dep]
     #D) file : priorité aux éléments de scores faibles
     file=filePrio()
     file=put(dep,score[dep],file)
     #E) parents
     parents={dep:None}
     plt.pause(0.1)
     carre(n)
     plt.plot(dep[0],dep[1],'bo')
     plt.plot(fin[0],fin[1],'bo')
     #F) Parcours
     while not empty(file):
          s,d=get(file) # sommet et distance au parent
          if s!=fin:
               for v,delta in G[s]:
                    # on cherche le sommet le plus proche de l'origine (chemin court)
                    # et le moins loin de l'arrivée
                    distance=distances_origine[s]+delta
                    if  distance<distances_origine[v]:
                         distances_origine[v]=distance
                         score[v]=distance+h[v]
                         file=put(v,distance+h[v],file)
                         parents[v]=s
                         plt.plot(v[0],v[1],"ro")
                         plt.pause(0.1)
                         input()
          else:
               plt.plot(s[0],s[1],'bo')
               chemin=[fin]
               while s!=dep:
                    s=parents[s]
                    chemin=[s]+chemin
                    plt.plot(s[0],s[1],'bo')
                    plt.pause(0.1)
               return distances_origine[fin],chemin



#################
### AVEC DES MURS
#################
          
def carre1(Murs):
     Abs=[]
     Ord=[]
     for (i,j) in Murs:
          Abs.append(i)
          Ord.append(j)
     return plt.plot(Abs,Ord,"k.")

def dico_voisins1(n,L):# avec les murs et distance=1
     V={}
     for i in range(2,n):
          for j in range(2,n):
               if (i,j) not in L:
                    V[(i,j)]=[[(i+1,j),1],[(i-1,j),1],[(i,j+1),1],[(i,j-1),1],[(i-1,j+1),1],[(i+1,j+1),1],[(i-1,j-1),1],[(i+1,j-1),1]]
     for s in V:
          V1=V[s][:]
          for x,y in V1:
               if x in L:
                    V[s].remove([x,y])
     for i in range(2,n):
          V[(i,1)]=[[(i-1,1),1],[(i,2),1],[(i+1,1),1],[(i-1,2),1],[(i+1,2),1]]
     for i in range(2,n):
          V[(i,n)]=[[(i-1,n),1],[(i,n-1),1],[(i+1,n),1],[(i-1,n-1),1],[(i+1,n-1),1]]
     for j in range(2,n):
          V[(1,j)]=[[(1,j-1),1],[(2,j),1],[(1,j+1),1],[(2,j+1),1],[(2,j-1),1]]
     for j in range(2,n):
          V[(n,j)]=[[(n,j-1),1],[(n-1,j),1],[(n,j+1),1],[(n-1,j-1),1],[(n-1,j+1),1]]
     V[(1,1)]=[[(1,2),1],[(2,1),1],[(2,2),1]]
     V[(n,1)]=[[(n-1,1),1],[(n,2),1],[(n-1,2),1]]
     V[(n,n)]=[[(n-1,n),1],[(n,n-1),1],[(n-1,n-1),1]]
     V[(1,n)]=[[(2,n),1],[(1,n-1),1],[(2,n-2),1]]
     return V

def algoA1(n,dep,fin,G): # G graphe avec murs
     visité={}
     visité[dep]=True
     for v in G:
          if v!=dep:
               visité[v]=False
     #A) distances à l'origine
     distances_origines={}
     distances_origine={dep:0}
     for v in G:
          if v!=dep:
               distances_origine[v]=float("inf")
     #B) heuristique : distance (euclidienne=vol oiseau) à la fin
     h={} # heuristique
     for v in G:
          h[v]=euclide(v,fin)
     #C) score=distance_origine+distance_fin
     score={}
     score[dep]=h[dep]+distances_origine[dep]
     ###TEST###
     for v in G:
          if v!=dep:
               score[v]=float("inf")
     ###TEST###
     #D) file : priorité aux éléments de scores faibles
     file=filePrio()
     file=put(dep,score[dep],file)
     #E) parents
     parents={dep:None}
     plt.pause(0.1)
     carre1(Murs)
     plt.plot(dep[0],dep[1],'bo')
     plt.plot(fin[0],fin[1],'bo')
     #F) Parcours
     while not empty(file):
          s,d=get(file) # sommet et distance au parent
          if s!=fin:
               for v,delta in G[s]:
                    if visité[v]==False:
                         dist=distances_origine[s]+delta
                         if  dist<distances_origine[v]:
                              distances_origine[v]=dist
                              score[v]=dist+h[v]
                              delete(file,v)
                              file=put(v,score[v],file)
                              parents[v]=s
                              plt.plot(v[0],v[1],"ro")
                              plt.pause(0.1)
                              visité[v]=True
          else:
               plt.plot(s[0],s[1],'bo')
               chemin=[fin]
               while s!=dep:
                    s=parents[s]
                    chemin=[s]+chemin
                    plt.plot(s[0],s[1],'bo')
                    plt.pause(0.1)
               return distances_origine[fin],chemin

# Mur1
L1=[(i,j) for i in range(14,17) for j in range(14,15)]
L2=[(i,j) for i in range(14,15) for j in range(14,17)]
L3=[(i,j) for i in range(16,17) for j in range(14,17)]
L4=[(i,j) for i in range(14,17) for j in range(13,14)]
L5=[(i,j) for i in range(13,14) for j in range(14,17)]
L6=[(i,j) for i in range(17,18) for j in range(14,17)]
L7=[(i,j) for i in range(5,13) for j in range(14,16)]

L=L1+L2#+L3+L4+L5+L6+L7




"""Pour tester les murs"""

"""
Murs=dico_voisins1(20,L)
algoA1(20,(5,5),(15,15),Murs)
"""

#Mur 2


"""
def algoAstar(n,dep,fin):#sans le dessin pour le cours
     visité={} #P
     G=dico_voisins(n)
     for v in G:
          visité[v]=False
     file=filePrio() #Q
     file=put(dep,euclide(dep,fin),file)
     distances_min={}
     distances_min={dep:0}
     h={}
     for v in G:
          h[v]=euclide(v,fin)
     scores_min={}
     scores_min[dep]=h[dep]+distances_min[dep]
     parents={dep:None}
     T=True
     while not empty(file) and T:
          s=get(file)[0] 
          if s==fin:
               T=False
          if visité[s]==False:
               for v in G[s]:
                    c=distances_min[s]+euclide(s,v)
                    if v not in scores_min or c<distances_min[v]:
                         distances_min[v]=c
                         scores_min[v]=c+h[v]
                         file=put(v,c+h[v],file)
                         parents[v]=s
          visité[s]=True
     s=fin
     chemin=[fin]
     while s!=dep:
          s=parents[s]
          chemin=[s]+chemin
     return distances_min[fin],chemin
 """              


     


