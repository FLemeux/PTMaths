D={}
D[1]=[3,5,4]
D[2]=[3]
D[3]=[1,2,4,5]
D[4]=[3,5,1]
D[5]=[4,1,3]
# 1 et 2 sont voisins
D[2].append(1)
D[1].append(2)
#print(D)
D[6]=[5,4]
D[4].append(6)
D[5].append(6)
#print(D)
D.pop(6)
for x in D : # on parcourt les clés
     D[x]=[v for v in D[x] if v!=6]
print(D)




