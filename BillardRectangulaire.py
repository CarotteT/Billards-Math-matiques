import numpy as np
import matplotlib.pyplot as plt 

#création de la table de billard rectangulaire
L=2
l=1
plt.plot([L,L,-L,-L,L],[l,-l,-l,l,l])
plt.axis('equal')

# conditions initiales
A=[0,-l ] #premier point
B=[L,0.3] #deuxième point
N=100 #nombre de rebonds
B[0]=L
angle=np.arctan(1*(L/l))
B[1]=np.tan(angle)/(L-A[1])
P=[]
ANGLE=[]
LONGUEUR=[]

# calcul de la succession des points d’impacts pour une condition initiale et un nombre de rebonds fixés 
for i in range(N):
    P.append(A)
    plt.plot([A[0],B[0]],[A[1],B[1]])
    C=[L,B[1]-(B[1]-A[1])/(B[0]-A[0])*(L-B[0])]
    D=[-L,B[1]-(B[1]-A[1])/(B[0]-A[0])*(-L-B[0])]
    E=[B[0]-(B[0]-A[0])/(B[1]-A[1])*(l-B[1]),l]
    F=[B[0]-(B[0]-A[0])/(B[1]-A[1])*(-l-B[1]),-l]
    A=B
    if C!=A and abs(C[1])<l:
        B=C
    if D!=A and abs(D[1])<l:
        B=D
    if E!=A and abs(E[0])<L:
        B=E
    if F!=A and abs(F[0])<L:
        B=F
        
plt.title('Trajectoire d une boule dans un billard rectangulaire')
plt.savefig('1.png')
plt.show()

# création du diagramme de phase
for i in range (N-1):
    ANGLE.append(angle)
    angle=np.pi/2-angle
    longueur=np.sqrt((P[i+1][0]-P[i][0])**2+(P[i+1][1]-P[i][1])**2)
    LONGUEUR.append(longueur)
    
plt.title('Portrait de phase du billard rectangulaire')
plt.xlabel('Position du point d impact')
plt.ylabel('Angle d indicdence')
plt.plot(LONGUEUR,ANGLE)
plt.savefig('2.png')
plt.show()
