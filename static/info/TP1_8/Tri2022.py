def placer(e,L):
    i=0
    k=len(L)
    while i<k and e>L[i]:
        i+=1
    return L[0:i]+[e]+L[i:k]

def triInsertion(L):
    n=len(L)
    for i in range(1,n):
        L=placer(L[i],L[:i])+L[i+1:]
        print(L)
    return L

def fusion(L1,L2):
    L=[]
    while len(L1)!=0 and len(L2)!=0:
        if L1[0]<L2[0]:
            L.append(L1.pop(0))
        else:
            L.append(L2.pop(0))
    return L+L1+L2

def triFusion(L):
    n=len(L)
    if n<=1:
        return L
    else:
        m=n//2
        L1=triFusion(L[:m])
        L2=triFusion(L[m:])
        return fusion(L1,L2)


def partition(L,g,d):
    pivot=L[g]
    c=1
    for i in range(1,d-g):
        if L[g+i]<pivot:
            L[g+i],L[g+c]=L[g+c],L[g+i] #r.a.s si i=c
            c+=1
    L[g],L[g+c-1]=L[g+c-1],L[g] # g+c-1 position pivot après partition
    return L[g:d],g+c-1


def triRapideRec(L,g,d):
    if len(L[g:d])<=1:
        return L[g:d]
    else:
        L[g:d],p=partition(L,g,d)
        return triRapideRec(L,g,p)+[L[p]]+triRapideRec(L,p+1,d)


def triRapide(L):
    n=len(L)
    if n<=1:
        return L
    else:
        L,p=partition(L,0,n)
        return triRapide(L[:p])+[L[p]]+triRapide(L[p+1:])




