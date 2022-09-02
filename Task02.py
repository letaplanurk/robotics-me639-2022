import numpy as np
import matplotlib.pyplot as plt

# constants for the problem

g = 9.81
l1= 10
l2= 10
theta=0
theta1=[1000]
theta2=[1000]
q1=np.pi/2
q2=0

om = 0
theta = np.pi/2
x=1
y=1
Fx=5
Fy=7


def manipulatorforce(t, y):
    '''
    func for the ODE solver - returns dy/dt of states
    '''
    om = y[1]
    theta = y[0]
    b = 0.1
    dydt = [om, -(g) * np.sin(theta) - b*om]
    return dydt


plt.ion()
plt.show()

for i in range(50):

    

    
    theta = np.arccos((x*x+y*y-l1*l1-l2*l2)/(2*l1*l2))
    q1=np.arctan(y/x)-np.arctan((l2*np.sin(theta))/(l1+l2*np.cos(theta)))
    q2=theta+q1
    x+=0.2
    y+=0.2
    
    theta1.append(q1)
    theta2.append(q2) 


    lp1 = (l1 * np.cos(theta1[i]), l2 * np.sin(theta1[i]))
    lp2 = (lp1[0]+l2 * np.cos(theta2[i]),lp1[1]+l2 * np.sin(theta2[i]))

    

    if round(lp2[0])==10:

        A=np.array([[l1 * np.cos(theta1[i]),-l1 * np.sin(theta1[i])],[l2 * np.cos(theta2[i]),-l2 * np.sin(theta2[i])]])
        B=np.array([[Fy],[-Fx]])
        C=np.dot(A,B)
        print(np.dot(A,B))
         
        print(lp2[0])
        break

    print(lp2[0])

    plt.clf() 


    plt.xlim([-20, 20])
    plt.ylim([-20, 20])

    # plot the manipulator.
    hinge = (0, 0)
    plt.plot([hinge[0], lp1[0]], [hinge[1], lp1[1]], '-o')
    plt.plot([lp1[0],lp2[0]],[lp1[1],lp2[1]], '-o')

    plt.axline((0, 10), (5, 10), linewidth=5, color='k')

    plt.pause(0.001)

plt.ioff()
plt.show()
