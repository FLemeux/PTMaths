
###Q1

"L=[1,5,8,12,14,16,53]"
"res=True"
"for i in range(1,len(L)):"
"     if L[i-1]>L[i]:"
"          res=False"
"print(res)"

###Q3

def mini(L):
     m=0
     for i in range(1,len(L)):
          if L[m]>L[i]:
               m=i
     return L[m]

###Q4

def creerPairImp(L):
     Pa=[]
     Imp=[]
     for i in range(len(L)):
          if L[i]%2==0:
               Pa.append(L[i])
          else:
               Imp.append(L[i])
     return Pa,Imp

def creerPairImp2(L):
     Pa=[]
     Imp=[]
     while len(L)>=1:
          if L[0]%2==0:
               Pa.append(L.pop(0))
          else:
               Imp.append(L.pop(0))
     return Pa,Imp

###Q12

def partition(L,g,d):
     c=1
     L1=L[g:d]
     pivot=L1[0]
     for i in range(1,len(L1)):
          if L1[i]<pivot:
               L1[i],L1[c]=L1[c],L1[i]
               c+=1
     L1[c-1],L1[0]=L1[0],L1[c-1]
     return g+c-1



