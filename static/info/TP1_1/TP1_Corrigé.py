"""
# TP1
# Ex1
# Q1
n=input("entrer un entier n : ")

# Q2
b=(n[0]==n[-1])

#Q3
#print(len(n)%2==0)

#Q4
m=n[-1]+n[1:len(n)-1]+n[0]

#Q5
d=len(n)
print(n[-1] in n[0:len(n)-1])
"""
"""
# Ex2
mot1=input("mot de 3 lettres : ")
print(mot1[0]==mot1[-1])
mot2=input("mot de 4 lettres : ")
print(mot2[0]==mot2[-1] and mot2[1]==mot2[-2])
mot3=mot1+mot2
mot4=mot3[0:3]
mot5=mot3[3:len(mot3)]

# Ex3
import math as m

a=int(input("1:disque/2:triangle/3:rectangle : "))
if a==1:
     r=float(input("entrer le rayon"))
     print(m.pi*r**2)
if a==2:
     b=float(input("entrer la base"))
     h=float(input("entrer la hauteur"))
     print(b*h/2)
if a==3:
     l=float(input("entrer largeur"))
     L=float(input("entrer longueur"))
     print(l*L)

# Ex4
a=float(input("entrer le coeff a"))
b=float(input("entrer le coeff b"))
c=float(input("entrer le coeff c"))
delta=b**2-4*a*c
if delta>0:
     print((-b+delta**0.5)/2/a,(-b-delta**0.5)/2/a)
elif delta==0:
     print(-b/2/a)
else:
     print((-b+1j*abs(delta)**0.5)/2/a,(-b-1j*delta**0.5)/2/a)
"""

"""
# Ex 5
n=int(input("entrer un entier naturel : "))
L=[]
for k in range(0,n+1,2):
     L.append(k)
print(L)
# ou
print(list(range(0,n+1,2)))

# Ex 6
n=int(input("entrer un entier naturel n : "))
S=0
for k in range(1,n+1):
     S+=k
print(S,n*(n+1)/2)

# Ex 7
L=[]
for i in range(1,n+1,2):
     if n%i==0:
          L.append(i)
print(L)
"""

"""
# Ex 8
n=int(input('entrer un entier n : '))
F=1 # F0
G=1 # F1
L0=[F]
L=[G/F]
for k in range(0,n):
     L0.append(G)
     L.append(G/F)
     # F=F_k, G=F_k+1
     F,G=G,F+G #F=F_k+1, G=F_k+2
     #ou
     #Gtemp=G
     #G=F+G
     #F=Gtemp
print(L0)
phi=(1+5**0.5)/2
print(L[len(L)-10:len(L)])
"""
