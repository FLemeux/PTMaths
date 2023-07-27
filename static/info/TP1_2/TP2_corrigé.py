# Exercice 1
def pairs(n):
     L=[] # liste vide 
     for k in range(1,n+1):
          if k%2==0:
               L.append(k)
     return L # on renvoie la liste

# Exercice 2

def diviseursImpairs(n):
     L=[]
     for k in range(1,n+1):
          if n%k==0 and k%2==1:
               L.append(k)
     return L

# Exercice 3
from math import *

def facto(n):
     p=1
     for k in range(1,n+1):
          p*=k # p=p*k
     return p

def bino(n,p):
     return int(facto(n)/(facto(p)*facto(n-p)))

#Ex4
def nenuphar(n):
     return 2**n

# Ex 5
#Q1
def F(n):
     F,G=1,1 # F=F0, G=F1
     for k in range(1,n+1):
          # F=F_(k-1), G=F_k
          F,G=G,F+G
          # F=F_k, G=F_(k+1)
     return F
#Q2
def listeF(n):
     L=[] # L=[F0]
     for k in range(0,n+1):
          L.append(F(k))
     return L

#Q3 :
phi=(1+5**0.5)/2 # psi=(1-5**0.5)/2
#Q4
L=listeF(50)
Lquotient=[]
"""
for k in range(0,50):
     Lquotient.append(L[k+1]/L[k])
#Q5
N=len(Lquotient)
print(Lquotient[N-10:N],phi)
####Conjecture :
# les quotients F_(n+1)/F_n convergent
# vers phi   ###
"""


# Exercice 6
#Q1
def suivant(N):
     if N%2==0: # N pair
          return N//2 # ou int(N/2)
     else: # N impair
          return 3*N+1
#Q2
def lesTermes(a,p):
     L=[a]
     for k in range(1,p+1):
          L.append(suivant(L[k-1]))
     return L

# Q3
def Temps(a):
     n=0
     while a!=1:
          n+=1
          a=suivant(a)
     return n



     























#
