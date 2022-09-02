
import numpy as np

l1 = 12;
l2 = 8;
m1 = 2
m2 = 2
r = 16;
g = 9.81;

x = -16
y = -16

def theta(x,y):
    theta = np.arccos((x**2+y**2-l1**2-l2**2)/(2*l1*l2))
    return(theta)

def q01(x,y):
    q1 = (np.arctan(y/x) - np.arctan(l2*np.sin(theta(x,y))/(l1+l2*np.cos(theta(x,y)))))
    return(q1)

def q02(x,y):
    q2 = q01(x,y) +theta(x,y)
    return(q2)

q1 = q01(x,y)
q2 = q02(x, y)
