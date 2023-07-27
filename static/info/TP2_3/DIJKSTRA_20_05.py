D={}
D['S']=[('T',8),('E',10),('L',5),('N',8)]
D['T']=[('S',8),('E',4)]
D['E']=[('T',4),('S',10),('L',8),('M',10)]
D['L']=[('E',8),('S',5),('N',2),('M',7)]
D['N']=[('S',8),('L',2),('M',4)]
D['M']=[('E',10),('L',7),('N',4)]

G={}
G['A']=[('B',12),('C',20),('D',9)]
G['B']=[('A',12),('G',13)]
G['C']=[('A',20),('D',8),('F',11),('G',7)]
G['D']=[('A',9),('C',8),('F',21)]
G['E']=[('F',3),('G',9)]
G['F']=[('C',11),('D',21),('E',3),('G',5)]
G['G']=[('B',13),('C',7),('F',5),('E',9)]

def filePrio(): # créé une file de priorité (vide pour l'instant)
     return []

def get(file): # supprime et renvoie l'élément en tête de file de plus forte priorité : celui de distance minimale à l'origine
     return file.pop()

def delete(file,element): # pour optimiser Dijkstra (sinon un sommet peut apparaitre avec plusieurs priorités, seule la minimal est exploitée 
     file1=[]
     for i in range(len(file)):
          if file[i][0]!=element:
               file1.append((file[i][0],file[i][1]))
     return file1

def put(file,element,priorite): # insère un élément à sa place en fonction de sa priorité
     i=0
     while i<len(file) and file[i][1]>priorite:
          i+=1
     return file[0:i]+[(element,priorite)]+file[i:len(file)]

def empty(file): # indique (booléen) si une file et vide
     return file==[]


def DIJKSTRA(G,dep,fin):
     parents={dep : None}
     dist_origine={dep : 0}
     for v in G:
          if v!=dep:
               dist_origine[v]=float("inf")
     chemin=[]
     file=filePrio()
     file=put(file,dep,0)
     while not empty(file):
          #print(file)
          (s,d)=get(file)
          if s!=fin:
               for v,delta in G[s]:
                    distance=delta+dist_origine[s]
                    if distance<dist_origine[v]:
                         file=delete(file,v)
                         file=put(file,v,distance)
                         parents[v]=s
                         dist_origine[v]=distance
          else:
               chemin=[fin]
               while s!=dep:
                    chemin.append(parents[s])
                    s=parents[s]
               chemin.reverse()
               return chemin,dist_origine[fin]
     return False


