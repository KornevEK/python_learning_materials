from math import e
import numpy as np
from matplotlib import pyplot as plt

def plot(f, a=-1, b=1):
    fig, ax = plt.subplots(figsize=(12, 8))
    x = np.linspace(a, b, num=64)
    ax.plot(x, f(x))
    plt.savefig('plt.png', dpi=400)
    plt.show()

def gen_sigmoid(eps):
    def sigmoid(x):
        return 1. / (1. + e ** (-x / eps))
    return sigmoid

def g(x):
    return 1.0

g = np.vectorize(g)

plot(g)

s = gen_sigmoid(0.1)

plot(s)
