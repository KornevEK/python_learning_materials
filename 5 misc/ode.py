import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Solver:
    def __init__(self, func):
        self.func = func
    def rk4_step(self, t: float, y: np.ndarray, h: float) -> np.ndarray:
        return y + h * self.func(t, y)
        # k1 = self.func(t, y)
        # k2 = self.func(t + .5 * h, y + .5 * k1)
        # k3 = self.func(t + .5 * h, y + .5 * k2)
        # k4 = self.func(t + h, y + k3)
        # return y + (h / 6.) * (k1 + 2. * k2 + 2. * k3 + k4)
    def solve(self, y0, t_list):
        y = y0
        y_list = [y0]
        for i in range(len(t_list) - 1):
            t_curr = t_list[i]
            t_next = t_list[i + 1]
            y = self.rk4_step(t_curr, y, t_next - t_curr)
            y_list.append(y)
        return np.stack(y_list)
    
    
# Lorenz system
sigma = 10
rho = 28
beta = 8. / 3.

func = lambda t, y: np.array([sigma * (y[1] - y[0]), y[0] * (rho - y[2]) - y[1], y[0] * y[1] - beta * y[2]])
y0 = np.array([2., 1., 1.])

solver = Solver(func)
frames = 2500
t_list = 0.01 * np.arange(frames)
y_list = solver.solve(y0, t_list)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection='3d')

ax.set_xlim(-20., 20.)
ax.set_ylim(-30., 30.)
ax.set_zlim(  0., 50.)

x = y_list[:, 0]
y = y_list[:, 1]
z = y_list[:, 2]

length = 100
line, = ax.plot(x[:length], y[:length], z[:length], 'b-', lw=5)

def update(i):
    # Update data for the line
    line.set_data(x[i:i+length], y[i:i+length])
    line.set_3d_properties(z[i:i+length])
    
    return line,

ax.plot(*y_list.T, 'k-', lw=0.1)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

anim = FuncAnimation(fig, update, frames=frames-length, interval=1, blit=True)
anim.save("ode_anim.gif", writer='pillow', fps=100)
# plt.show()
