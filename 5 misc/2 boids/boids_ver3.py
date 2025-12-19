import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numba import jit, njit

import sys

@njit(inline='always')
def dist_jit(p1, p2):
    return np.linalg.norm(p1 - p2)

@jit(cache=True)
def update_boids_jit(p, v, NUMBER=100):
    
    DELTA_T = 0.01
    
    XLIM = 100
    YLIM = 100

    SPEED = 100
    VISION = 10

    alpha = .5
    beta  = 1.0
    gamma = .2
    
    com = np.sum(p, axis=0) / p.shape[0]
    v_n = v.copy()
    
    for i in range(NUMBER):
        # rule 1
        com_i = (com * NUMBER - p[i]) / (NUMBER - 1)
        v_n[i] += alpha * (com_i - p[i])
        for j in range(NUMBER):
            d = dist_jit(p[i], p[j])
            dv = np.zeros(NUMBER)
            neigh = 1
            if (i != j) and (d < VISION):
                # rule 2
                v_n[i] -= beta * (p[j] - p[i]) / d
                # rule 3
                dv += v[j]
                neigh += 1
        v_n[i] += gamma * dv / (neigh)
    v = SPEED * v_n / ((v_n[:, 0]**2 + v_n[:, 1]**2)**.5)[:, None]
    # self.v[:, 0] = np.where(np.abs(self.p[:, 0] - self.XLIM / 2) < self.XLIM / 2, self.v[:, 0], -self.v[:, 0])
    # self.v[:, 1] = np.where(np.abs(self.p[:, 1] - self.YLIM / 2) < self.YLIM / 2, self.v[:, 1], -self.v[:, 1])
    p += DELTA_T * v
    #p = np.remainder(p, [XLIM, YLIM])
    p[:, 0] = np.where(p[:, 0] > 0, p[:, 0], p[:, 0] + XLIM)
    p[:, 0] = np.where(p[:, 0] < XLIM, p[:, 0], p[:, 0] - XLIM)
    p[:, 1] = np.where(p[:, 1] > 0, p[:, 1], p[:, 1] + YLIM)
    p[:, 1] = np.where(p[:, 1] < YLIM, p[:, 1], p[:, 1] - YLIM)
        
    return p, v
    
class Boids:
    
    def __init__(self, NUMBER):
        self.DELTA_T = 0.01
        
        self.XLIM = 100
        self.YLIM = 100

        self.SPEED = 100
        self.VISION = 10

        self.NUMBER = NUMBER

        self.alpha = 0.5
        self.beta  = 1.0
        self.gamma = .2
        
        self.p = np.random.multivariate_normal([.5*self.XLIM, .5*self.YLIM], [[self.XLIM, 0.], [0., self.YLIM]], self.NUMBER)
        self.v = np.random.multivariate_normal([0., 0.], [[1., 0.], [0., 1.]], self.NUMBER)
        self.v = self.SPEED * self.v / np.linalg.norm(self.v, axis=1)[:, None]
    
    def plot(self):
        
        # Create new Figure with black background
        fig = plt.figure(figsize=(8, 8), facecolor='black')

        # Add a subplot with no frame
        ax = plt.subplot(frameon=False)

        # Generate line plots
        self.sc = ax.quiver(self.p[:, 0], self.p[:, 1], 
                            self.v[:, 0], self.v[:, 1],
                            color='blue')
        
        self.sc_white = ax.quiver(self.p[:, 0], self.p[:, 1], 
                            self.v[:, 0], self.v[:, 1],
                            color='white', alpha=(self.v[:, 0])**2 / 100**2)

        # Set y limit (or first line is cropped because of thickness)
        ax.set_xlim(0., self.XLIM)
        ax.set_ylim(0., self.YLIM)

        # No ticks
        ax.set_xticks([])
        ax.set_yticks([])

        def update(*args):
            
            # self.update_boids()
        
            p, v = self.p, self.v
            p, v = update_boids_jit(p, v, self.NUMBER)
            self.p, self.v = p, v
            
            self.sc.set_offsets(self.p)
            self.sc.set_UVC(self.v[:, 0], self.v[:, 1])
            
            self.sc_white.set_offsets(self.p)
            self.sc_white.set_UVC(self.v[:, 0], self.v[:, 1])
            self.sc_white.set_alpha((self.v[:, 0])**2 / 100**2)
            
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
    
    
