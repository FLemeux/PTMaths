from random import *


def listeAleatoire(n):
     return [randint(0,n) for k in range(n//2)]



def triInsertion(L):
     k=len(L)
     for i in range(2,k):
          c=0
          while L[i]>L[c]:
               c+=1
          L.insert(c,L.pop(i))
     return L


def fusion(L1,L2):
     L=[]
     while len(L1)!=0 and len(L2)!=0:
          if L1[0]<L2[0]:
               L.append(L1.pop(0))
          else:
               L.append(L2.pop(0))
     if len(L1)!=0:
          L+=L1
     else:
          L+=L2
     return L

def triFusion(L):
     if len(L)<=1:
          return L
     m=len(L)//2
     return fusion(triFusion(L[m:]),triFusion(L[:m]))

def partition(L,g,d):
     c=1
     pivot=L[g]
     for i in range(1,len(L[g:d])):
          if L[g+i]<pivot:
               L[g+i],L[g+c]=L[g+c],L[g+i]
               c+=1
     L[g+c-1],L[g]=L[g],L[g+c-1]
     return g+c-1

def triRapideRec(L,g,d):
     if len(L[g:d])<=1:
          return L[g:d]
     p=partition(L,g,d)
     return triRapideRec(L,g,p)+[L[p]]+triRapideRec(L,p+1,d+1)


