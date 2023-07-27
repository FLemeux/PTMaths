     
### PARTIE I : EXERCICES BASIQUES ###

def puissanceBasique(x,n):
    A=1
    for i in range(n):
        A=x*A
    return A

def puissanceRapide(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return puissanceRapide(x,n/2)**2
    else:
        return x*puissanceRapide(x,(n-1)/2)**2
    
def miroir(x):
    if len(x)==1:
        return x
    else:
        x=x[-1]+miroir(x[:-1])
        return x



def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b,a%b)

def appartient(x,L):
    n=len(L)
    if n==0:
        return False
    elif n==1:
        return L[0]==x
    else:
        if L[n//2]==x:
            return True
        elif L[n//2]>x:
            return appartient(x,L[0:n//2])
        else:
            return appartient(x,L[n//2+1:n])

def base2(N):
    if N==0:
        return ""
    elif N==1:
        return "1"
    else:
        if N%2==0:
            return base2(N//2)+"0"
        else:
            return base2(N//2)+"1"

####II - CATALAN####
        
def K(n):
    if n==0:
        return 1
    else:
        S=0
        for i in range(n):
            S+=K(i)*K(n-i-1)
        return S

import time

L=[]

#for k in range(12,17):
#    t=time.time()
#    K(k)
#    L.append(time.time()-t)

#R=[]
#for i in range(len(L)-1):
#    R.append(L[i+1]/L[i])

#C(n)=2(C(0)+...+C(n-1))+n(mult)+(n-1)(add)
#C(n+1)=3C(n)+2 : C(n)=3^n-1

def LK(n):
    L=[1]
    for k in range(1,n+1):
        S=0
        for i in range(k):
            S+=L[i]*L[k-1-i]
        L.append(S)
    return L
    
from scipy.misc import *

def L(n):
    return int(1/(n+1)*comb(2*n,n))

#print(LK(9))
#print([L(k) for k in range(10)])

def Knew(n):
    P=1
    for k in range(1,n):
        P=(2*k+2)*(2*k+1)/((k+2)*(k+1))*P
    return int(P)


def MotsDyckRecursif(n):
    if n==0:
        return ["",]
    if n==1:
        return ["AB",]
    else:
        L=[]
        for i in range(n):
            sousmot1=MotsDyckRecursif(i)
            sousmot2=MotsDyckRecursif(n-i-1)
            for mot1 in sousmot1:
                for mot2 in sousmot2:
                    L.append("A"+mot1+"B"+mot2)
                    #print(L)
        return L

##Algo itératif non demandé et plus long : 

def base2(n):
    L=[]
    if n==0:
        L=[0]
    else:
        while n>=1:
            L.append(n%2)
            n=n//2
        L.reverse()
    return L

def mots_binaires(n):
    L=[]
    for k in range(4**n):
        l=base2(k)
        lg=len(l)
        L.append((2*n-lg)*[0]+l)
    return L

def est_Dyck(mot):
    c_a,c_b,n=0,0,0
    l=len(mot)
    while c_a>=c_b and n<l:
        if mot[n]=="A":
            c_a+=1
        else:
            c_b+=1
        n+=1
    if l==n and c_a==c_b:
        return True
    else:
        return False

def conversion(L):
    for k in range(len(L)):
        if L[k]==0:
            L[k]="B"
        else:
            L[k]="A"
    s=""
    for val in L:
        s+=val
    return s

def liste_mots(n):
    return [conversion(mot) for mot in mots_binaires(n)]

def mots_Dyck(n):
    return [mot for mot in liste_mots(n) if est_Dyck(mot)]


####III - BONS MOTS####

def uEx3(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return 2*uEx3(n-1)-uEx3(n-2)+uEx3(n-3)

def mot(N):
    if N==1:
        return [[0],[1]]
    else:
        L=mot(N-1)
        K=[]
        for l in L:
            k=l[:]
            l.append(0)
            k.append(1)
            K.append(l)
            K.append(k)
    return K


def bonMot(L):
    c=0
    n=len(L)
    T=[]
    if L[0]==1:
        T.append(L[1]==1)
    for i in range(1,n-1):
        if L[i]==1:
            T.append(L[i-1]==1 or L[i+1]==1)
    if L[-1]==1:
                 T.append(L[-2]==1)
    B=True #pour ne casser la boucle for
    for b in T:
        if not b:
            B=False
    return B

def lesBonMots(N):
    return [m for m in mot(N) if bonMot(m)]

#for n in range(2,16):
#    print(len(lesBonMots(n))==uEx3(n))



####IV - PAYER EN JETONS####

def P5(n):
    if n%5==0:
        return 1
    else:
        return 0
    #ou int(n%5==0)

def P25(n):
    C=0
    for k in range(n//2+1):
        C+=P5(n-2*k)
        #print(k,C)
    return C

def P125(n):
    C=0
    for k in range(n+1):
        C+=P25(n-k)
    return C

def P(V,n):
    if len(V)==1:
        return int(n%V[0]==0)
    else:
        j=V[0]
        C=0
        W=V[1:]
        for k in range(n//j+1):
            C+=P(W,n-k*j)
    return C

def P2(V,n):
    V.reverse()
    return P(V,n)

        
