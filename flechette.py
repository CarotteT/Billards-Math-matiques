import numpy as np
import matplotlib.pyplot as plt

R0=1

#Question 1

def raduis(x,y,r):
    return np.sqrt(r**2-(x**2+y**2))

#Question 2

def play(R0):
    score=0
    x=np.random.uniform(-R0,R0)
    y=np.random.uniform(-R0,R0)
    if x**2+y**2 >R0:
        exit
    else :
        score=score+1
        R0=raduis(x,y,R0)
        x=np.random.uniform(-R0,R0)
        y=np.random.uniform(-R0,R0)
    return score

#Question 3
    
def draw_circle(x,y,r,col):
    c=np.arange(0,2*np.pi+np.pi/10,np.pi/10)
    circle=plt.plot(r*np.cos(c),r*np.sin(c),col);plt.plot(x,y,'o'+col)
    return circle


#Question 4

def coord(r,theta):
    return [r*np.cos(theta),r*np.sin(theta)]

#Question 5
    
def draw_chord(x,y,r,col):
    r1=raduis(x,y,r)
    a=np.arctan2(y,x)
    b=np.arcsin(r1/r)
    theta1=a+b
    theta2=a-b
    p1=coord(r,theta1)
    p2=coord(r,theta2)
    chord=plt.plot(p1,p2)
    return chord

#Question 6
    
def play_graph(R0):
    color=['b','g','r','c','m','y']
    r=R0
    draw_circle(0,0,r,'b')
    score=0
    i=0
    x=np.random.uniform(-R0,R0)
    y=np.random.uniform(-R0,R0)
    if x**2+y**2 >R0:
        exit
    else :
        i+=1
        score=score+1
        R0=raduis(x,y,R0)
        x=np.random.uniform(-R0,R0)
        y=np.random.uniform(-R0,R0)
        draw_cord
    
    return

#Question 8
    
score1000=np.ones(1000)
for i in range (0,1000):
    score1000[i]=play(R0)
    
plt.hist(score1000)
print(np.mean(score1000))
