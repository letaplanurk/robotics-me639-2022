import numpy as np
import matplotlib.pyplot as plt

# constants

g = 9.81
l1= 7
l2= 7
theta=0
theta1=[1000]
theta2=[1000]
q1=np.pi/2
q2=0

omega = 0
theta = np.pi/2
x=1
y=1
Fx=2
Fy=3


def pendulumModel(t, y):
    '''
    function for the ODE solver - returns dy/dt of states
    '''
    omega = y[1]
    theta = y[0]
    b = 0.1
    dydt = [omega, -(g) * np.sin(theta) - b*omega]
    return dydt


plt.ion()
plt.show()

for i in range(100):

    

    
    theta = np.arccos((x*x+y*y-l1*l1-l2*l2)/(2*l1*l2))
    q1=np.arctan(y/x)-np.arctan((l2*np.sin(theta))/(l1+l2*np.cos(theta)))
    q2=theta+q1
    x+=0.2
    y+=0.2
    
    theta1.append(q1)
    theta2.append(q2) 


    linkpos1 = (l1 * np.cos(theta1[i]), l2 * np.sin(theta1[i]))
    linkpos2 = (linkpos1[0]+l2 * np.cos(theta2[i]),linkpos1[1]+l2 * np.sin(theta2[i]))

    

    if round(linkpos2[0])==10:

        A=np.array([[l1 * np.cos(theta1[i]),-l1 * np.sin(theta1[i])],[l2 * np.cos(theta2[i]),-l2 * np.sin(theta2[i])]])
        B=np.array([[0.5 * (l1 * np.sin(theta1[i])+l2 * np.sin(theta2[i]))],[-0.5 * (l1 * np.cos(theta1[i])+l2*np.cos(theta2[i]))]])
        M=np.array([[Fy],[-Fx]])
        C=np.dot(A,B)
        D=np.dot(A,M)
        print(np.dot(A,B))
        print(np.dot(A,M))
        hinge = (0, 0)
        plt.plot([hinge[0], linkpos1[0]], [hinge[1], linkpos1[1]], '-o')
        plt.plot([linkpos1[0],linkpos2[0]],[linkpos1[1],linkpos2[1]], '-o')
         
        print(linkpos2[0])
        break

    print(linkpos2[0])

    plt.clf()

    plt.xlim([-20, 20])
    plt.ylim([-20, 20])

    hinge = (0, 0)
    plt.plot([hinge[0], linkpos1[0]], [hinge[1], linkpos1[1]], '-o')
    plt.plot([linkpos1[0],linkpos2[0]],[linkpos1[1],linkpos2[1]], '-o')

    plt.axline((0, 20), (10, 10), linewidth=10, color='r')

    plt.pause(0.0001)

plt.ioff()
plt.show()



