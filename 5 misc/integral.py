import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sqrt(1. - x**2)

def trapezoid(n):
    x = np.linspace(0., 1., n)
    h = 1. / (n - 1)
    y = f(x)
    y_left  = y[:-1]
    y_right = y[1: ]
    return h * np.sum(y_left + y_right) / 2

def midpoint(n):
    x = np.linspace(0., 1., n)
    h = 1. / (n - 1)
    x_mid = (x + h/2)[:-1]
    y_mid = f(x_mid)
    return h * np.sum(y_mid)

def monte_carlo(n):
    points = np.random.uniform(0., 1., (n, 2))
    points = np.where(points[:, 0]**2 + points[:, 1]**2 < 1., 1., 0.)
    return np.sum(points) / points.shape[0]

if __name__ == "__main__":
    S = np.pi / 4
    n_list = 2 ** np.arange(1, 25)
    midpoint_errors = [np.abs(midpoint(n) - S) for n in n_list]
    trapezoid_errors = [np.abs(trapezoid(n) - S) for n in n_list]
    monte_carlo_errors = [np.abs(monte_carlo(n) - S) for n in n_list]
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.loglog(n_list, midpoint_errors, label='Midpoint rule')
    ax.loglog(n_list, trapezoid_errors, label='Trapezoid')
    ax.loglog(n_list, monte_carlo_errors, label='Monte-Carlo')
    ax.loglog(n_list, 1 / np.sqrt(n_list), "k--", label=r'$\frac{1}{\sqrt{N}}$')
    ax.loglog(n_list, 1 / n_list**2, "k-.", label=r'$\frac{1}{n^2}$')
    plt.legend(fontsize=15)
    plt.show()