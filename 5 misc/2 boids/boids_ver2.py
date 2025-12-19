import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numba import jit, njit

import sys

@njit(inline='always')
def dist_jit(p1, p2):
    return np.linalg.norm(p1 - p2)
    
class Boids:
    
    def __init__(self, NUMBER):
        self.DELTA_T = 0.01
        
        self.XLIM = 100
        self.YLIM = 100

        self.SPEED = 100
        self.VISION = 10

        self.NUMBER = NUMBER

        self.alpha = .5
        self.beta  = 1.0
        self.gamma = .2
        
        self.p = np.random.multivariate_normal([.5*self.XLIM, .5*self.YLIM], [[self.XLIM, 0.], [0., self.YLIM]], self.NUMBER)
        self.v = np.random.multivariate_normal([0., 0.], [[1., 0.], [0., 1.]], self.NUMBER)
        self.v = self.SPEED * self.v / np.linalg.norm(self.v, axis=1)[:, None]

    def update_boids(self):
        com = np.mean(self.p, axis=0)
        v_n = self.v.copy()
        
        for i in range(self.NUMBER):
            # rule 1
            com_i = (com * self.NUMBER - self.p[i]) / (self.NUMBER - 1)
            v_n[i] += self.alpha * (com_i - self.p[i])
            for j in range(self.NUMBER):
                d = dist_jit(self.p[i], self.p[j])
                dv = 0
                neigh = 1
                if (i != j) and (d < self.VISION):
                    # rule 2
                    v_n[i] -= self.beta * (self.p[j] - self.p[i]) / d
                    # rule 3
                    dv += self.v[j]
                    neigh += 1
            v_n[i] += self.gamma * dv / (neigh)
        self.v = self.SPEED * v_n / np.linalg.norm(v_n, axis=1)[:, None]
        # self.v[:, 0] = np.where(np.abs(self.p[:, 0] - self.XLIM / 2) < self.XLIM / 2, self.v[:, 0], -self.v[:, 0])
        # self.v[:, 1] = np.where(np.abs(self.p[:, 1] - self.YLIM / 2) < self.YLIM / 2, self.v[:, 1], -self.v[:, 1])
        self.p += self.DELTA_T * self.v
        self.p = np.remainder(self.p, [self.XLIM, self.YLIM])
    
    def plot(self):
        
        # Create new Figure with black background
        fig = plt.figure(figsize=(8, 8), facecolor='black')

        # Add a subplot with no frame
        ax = plt.subplot(frameon=False)

        # Generate line plots
        self.sc = ax.quiver(self.p[:, 0], self.p[:, 1], 
                            self.v[:, 0], self.v[:, 1],
                            self.v[:, 0])

        # Set y limit (or first line is cropped because of thickness)
        ax.set_xlim(0., self.XLIM)
        ax.set_ylim(0., self.YLIM)

        # No ticks
        ax.set_xticks([])
        ax.set_yticks([])

        def update(*args):
            
            self.update_boids()
            
            self.sc.set_offsets(self.p)
            self.sc.set_UVC(self.v[:, 0], self.v[:, 1])
            
            # Return modified artists
            return self.sc

        # Construct the animation, using the update function as the animation director.
        anim = animation.FuncAnimation(fig, update, interval=1, save_count=100)
        plt.show()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) > 0:
        b = Boids(int(sys.argv[1]))
    else:
        b = Boids(20)
    b.plot()
    
    
