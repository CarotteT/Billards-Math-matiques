import numpy as np
import matplotlib.pyplot as plt

# création de la table de billard tronquée
n=3
theta=np.linspace(np.pi/n,2*np.pi-np.pi/n,100)
troncature=np.pi/n
r=np.sqrt(1)
X1=r*np.cos(theta)
X2=r*np.sin(theta)
P=0 
plt.plot(X1,X2)
plt.plot([X1[0],X1[-1]],[X2[0],X2[-1]])
plt.axis('equal')

# conditions initiales
A=np.array([-1,0])
B=np.array([0,0])
angle=np.pi/9 #par rapport à la normal
hauteur=r*np.sin(angle) #hauteur d'un triangle isocèle
longueur = 2*np.sqrt(r**2-hauteur**2) #longueur entre deux points
N=1 #nombre de tour de cercle
C=0 #nombre de rebond
Theta=np.linspace(0,2*np.pi*N,10000)
x1=r*np.cos(Theta)
x2=r*np.sin(Theta)
S=np.array([])
    
    
while C<10:
    for i in range(10000):
        if longueur-0.005 <np.sqrt((x1[i]-A[0])**2+(x2[i]-A[1])**2) < longueur+0.005 :
            B=np.array([x1[i],x2[i]])
            if 0.5<x1[i]<1 :
                D=np.array([X1[0],x2[i]])
                Vectab=np.array([A[0]-B[0],A[1]-B[1]])/np.linalg.norm(np.array([A[0]-B[0],A[1]-B[1]]))
                Vectcb=np.array([D[0]-B[0],D[1]-B[1]])/np.linalg.norm(np.array([D[0]-B[0],D[1]-B[1]])) 
                angle2=np.arccos(np.vdot(Vectab,Vectcb))
                longueurcB=np.tan(angle2)*np.sqrt((D[0]-B[0])**2+(D[1]-B[1])**2)
                E=np.array([x1[0],longueurcB-D[1]])
                plt.plot([A[0],E[0]],[A[1],E[1]])
                C+=1
                P=E[1]-np.tan(angle2)*E[0]
                for i in range(10000):
                    if x1[i]**2+x2[i]**2==1 and x2[i]==np.tan(angle2)*x1[i]+P :
                        F=np.array([x1[i],x2[i]])
                        #plt.plot([E[0],F[0]],[E[1],F[1]])
                        C+=1
                        A=F
            else :
                #plt.plot([A[0],B[0]],[A[1],B[1]])
                s=np.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
                A=B
                S=np.append(S,s)
                C+=1
                P=np.append(P,B)
                
plt.title('Trajectoire d une boule dans un billard tronqué')
plt.savefig('5.png')
plt.show()

plt.title('Portrait de phase du billard tronqué')
plt.xlabel('Position du point d impact')
plt.ylabel('Angle d indicdence')
plt.plot(S,np.ones(len(S))*np.sin(angle))
plt.savefig('6.png')
plt.show()
