import numpy as np
import matplotlib.pyplot as plt

###Q2

def lecture(nom):
    fichier=open(nom,'r')
    data=[]
    for ligne in fichier:
        data.append(ligne.split(";"))
    data.pop(0)
    data.pop(0)
    
    lesT=[]
    lesE=[]
    lesS=[]
    for serie in data:
        lesT.append(float(serie[0]))
        lesE.append(float(serie[1]))
        lesS.append(float(serie[2]))
    return [lesT,lesE,lesS]

###Q3

def trace(nom):
    lesT=lecture(nom)[0]
    lesE=lecture(nom)[1]
    lesS=lecture(nom)[2]
    plt.plot(lesT,lesE,'b',label='Entrée')
    plt.plot(lesT,lesS,'r',label='Sortie')
    plt.title(r'$\Omega$ = '+str(pulsation(nom))+r' $rad.s^{-1}$')
    plt.xlabel('Temps')
    plt.legend()
    plt.show()
    
###Q4

def pulsation(nom):
    lesChgt=[]
    lesT=lecture(nom)[0]
    lesE=lecture(nom)[1]
    c=0
    while len(lesChgt) < 3:
        if lesE[c]*lesE[c+1] < 0:
            lesChgt.append((lesT[c]+lesT[c+1])/2)
        c+=1
    return 2*np.pi/(lesChgt[2]-lesChgt[0])
    
###Q6

def maximum(L):
    m=L[0]
    for k in L:
        if k>m:
            m=k
    return m

###Q8

def gain(nom):
    lesE=lecture(nom)[1]
    lesS=lecture(nom)[2]
    return maximum(lesS)/maximum(lesE)

###Q10

def dephasage(nom):
    lesT=lecture(nom)[0]
    lesE=lecture(nom)[1]
    lesS=lecture(nom)[2]
    i,j=1,1
    while lesE[i]*lesE[i+1]>0 and lesE[i]<lesE[i+1]:
        i+=1
        j+=1
    while lesS[j]*lesS[j+1]>0 and lesS[j]<lesS[j+1]:
        j+=1
    deltaT=lesT[i]-lesT[j]
    return deltaT*pulsation(nom)

###Q11


lesW=[]
lesG=[]
lesPhi=[]

for k in range(60):
    fichier="mesure"+str(k)+".txt"
    lesW.append(pulsation(fichier))
    lesG.append(gain(fichier))
    lesPhi.append(180/np.pi*dephasage(fichier))

    lesGdB=[20*np.log10(k) for k in lesG]

plt.subplot(2,1,1)
plt.plot(lesW,lesGdB)
plt.title("Gain en dB")
plt.xscale('log')

plt.subplot(2,1,2)
plt.plot(lesW,lesPhi)
plt.title("Phase en rad")
plt.xscale('log')

plt.show()


