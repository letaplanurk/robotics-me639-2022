
import numpy as np
from task_1_sub import q01 ,q02, r,l1 ,l2
import matplotlib.pyplot as plt
from matplotlib import animation

t = np.linspace(0, 30, 501)
angle = np.linspace(0, 2*np.pi, 501)
x = r*np.cos(angle)
y = r*np.sin(angle)

q1 = q01(x,y)
q2 = q02(x,y)

def get_coordinates(t, q1, q2, p1, p2):
    return(l1*np.cos(q1),
           l2*np.sin(q1),
           l1*np.cos(q1)+l2*np.sin(q2), 
           l1*np.sin(q1)+l2*np.sin(q2)
        )
x1, y1, x2, y2 = get_coordinates(t, q1, q2, l1, l2)

def animate(i):
    ln1.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    
fig, ax = plt.subplots(1,1, figsize=(8,8))
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ln1, = plt.plot([], [], 'ro-' , lw=3, markersize=8)
ax.set_ylim(-30,30)
ax.set_xlim(-30,30)
ani = animation.FuncAnimation(fig, animate, frames=500, interval=50)
ani.save('Task.gif', writer='pillow', fps=60)