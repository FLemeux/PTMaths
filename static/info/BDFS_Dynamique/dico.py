D={}
D[1]=[3,4,5]
D[2]=[3]
D[3]=[2,1,5,4]
D[4]=[1,5,3]
D[5]=[3,1,4]
"""
print(D)
print("liste adjacence de 3 : ",D[3])
print(len(D))
"""

"""
for x in D:
     print(x)
for y in D.items():
     print(y)
for z in D.keys():
     print(z)
for t in D.values():
     print(t)
"""

D[6]=[4,5]
print(D)
D[4].append(6)
D[5].append(6)
D[1].append(2)
D[2].append(1)
print(D)
D.pop(6)
print(D)
for x in D:
     D[x]=[v for v in D[x] if v!=6]
print(D)
