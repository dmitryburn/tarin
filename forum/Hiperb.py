from matplotlib.animation import writers
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

BOUNDS_X = (-20.2, 20.2)
BOUNDS_Y = (-20.2, 20.2)

class Parabolic:
    def __init__(self, p):
        self.p1_p = p

        self.fig = plt.figure()
        self.ax = plt.axes(xlim=BOUNDS_X, ylim=BOUNDS_Y)

        self.rocket, = self.ax.plot([], [], marker='o', markersize=4, markerfacecolor='red', label='Rocket')
        self.rocket_o, = self.ax.plot([], [], color='w', lw=1.5)

        self.t = np.linspace(-np.pi/2+0.0001, np.pi/2-0.0001, 361)[::-1]

        self.x1 = self.p1_p / (1 - np.sin(self.t)) * np.cos(self.t)
        self.y1 = self.p1_p / (1 - np.sin(self.t)) * np.sin(self.t)
        self.x1 = np.array(list(-1 * self.x1) + list(self.x1[::-1]))
        self.y1 = np.array(list(self.y1) + list(self.y1[::-1]))

    def solar_system(self, i):
        self.rocket.set_data(self.x1[i], self.y1[i])
        self.rocket_o.set_data(self.x1[:i], self.y1[:i])
        return self.rocket, self.rocket_o
    
    def visualize(self):
        anim = animation.FuncAnimation(self.fig, self.solar_system, frames=2*len(self.t), interval=25, blit=True, repeat=True)
        self.fig.patch.set_facecolor('k')
        self.fig.tight_layout()
        plt.plot(0, self.p1_p / (1 - np.sin(3*np.pi / 2)) * np.sin(3 * np.pi / 2) + self.p1_p / 2, 'yo', markersize=6.5, label='Moon')
        plt.axis(False)
        plt.legend()
        plt.show()

if __name__ == '__main__':
    pr = Parabolic(4)
    pr.visualize()
