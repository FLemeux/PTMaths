def binaire(n):
     L=[]
     while n>0:
          L=[n%2]+L
          n=n//2
     return L

def rechercheDicho(x,a):
     g,d=0,len(a)-1
     while d>=g:
          m=(g+d)//2
          if a[m]==x:
               return True
          elif x<a[m]:
               d=m-1
          else:
               g=m+1
     return False

def recherche(a,x):
     for y in a:
          if y==x:
               return True
     return False


D={}
























               
D={} # accolades

D["Rennes"]=["Paris","Lyon"]  # liste d'adjacence (voisins de Rennes)
D["Paris"]=["Rennes","Lyon"] # il n'y a pas d'ordre
D["Lyon"]=["Paris","Rennes","Nantes"]
D["Nantes"]=["Lyon"]

for x in D:
     print(x)

for x in D.keys():
     print(x)

for x in D.values():
     print(x)

for x in D.items():
     print(x)










