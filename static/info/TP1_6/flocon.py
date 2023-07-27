import matplotlib.pyplot as plt
import numpy as np

R=np.array([[np.cos(np.pi/3),-np.sin(np.pi/3)],[np.sin(np.pi/3),np.cos(np.pi/3)]])

def von(n,A,B):
    if n==0:
        plt.plot([A[0],B[0]],[A[1],B[1]],'-b')
    else:
        A1=A+(B-A)/3
        A3=A+(B-A)/3*2
        A2=A1+R.dot(A1-A)
        von(n-1,A,A1)
        von(n-1,A1,A2)
        von(n-1,A2,A3)
        von(n-1,A3,B)

def tracer(n,A,B):
    von(n,A,B)
    plt.figure(1, figsize=(8, 8))
    return plt.show()
