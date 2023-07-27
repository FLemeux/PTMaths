# Récursivité

#Exercice 1
#Q1. Version itérative
def fact(n):
     p=1
     for k in range(2,n+1):
          p=p*k
     return p

#Q1. Version récursive
def factRec(n):
     if n==1:
          return 1
     else:
          return n*factRec(n-1)
     

# Q2 Itérative

def u(n):
     u=2 # u_0=2
     for k in range(1,n+1):
          # u = u_{k-1}
          u=u/2+1/u
          # u= u_k
     return u # u=u_n
# Q2 Version récursive
def uRec(n):
     if n==0:
          return 2
     else:
          return uRec(n-1)/2+1/uRec(n-1)

# Q4 Nb de zéros dans une liste

def nbZeros(L):
     c=0
     for k in range(len(L)):
          if L[k]==0:
               c+=1
     return c

def nbZeros1(L):
     c=0
     for x in L:
          if x==0:
               c+=1
     return c

def nbZerosRec(L):
     if L==[]:
          return 0
     else:
          if L[0]==0:
               return 1+nbZerosRec(L[1:len(L)])
          else:
               return nbZerosRec(L[1:len(L)])
     



















