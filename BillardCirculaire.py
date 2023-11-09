import numpy as np
import matplotlib.pyplot as plt

# création de la table de billard circulaire
r=np.sqrt(1)
a=np.linspace(0,2*np.pi,100)
x1=np.cos(a)*r
x2=np.sin(a)*r
plt.plot(x1,x2)
plt.axis('equal')

# conditions initiales
A=np.array([0,-1])
B=np.array([0,0])
N=150 #nombre de rebonds
C=25 #nombre de tours de cercle
angle=(C/N)*np.pi
hauteur=np.sin(angle)*r
longueur=2*np.sqrt(r**2-hauteur**2)

theta=np.linspace(0,0.2*np.pi*N,1000)
x1=np.cos(theta)*r
x2=np.sin(theta)*r
S=np.array([])

while C<100:
    for i in range(1000):
        if longueur-0.5 < np.sqrt((x1[i]-A[0])**2+(x2[i]-A[1])**2) < longueur+0.5 :
            B=np.array([x1[i],x2[i]])
            plt.plot([A[0],B[0]],[A[1],B[1]])
            s=np.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
            A=B
            C+=1
            S=np.append(S,s)
        
plt.title('Trajectoire d une boule dans un billard circulaire')
plt.savefig('3.png')
plt.show()

plt.title('Portrait de phase du billard circulaire')
plt.xlabel('Position du point d impact')
plt.ylabel('Angle d indicdence')
plt.plot(S,np.ones(len(S))*np.sin(angle))
plt.savefig('4.png')
plt.show()
