import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    with open("input.txt", 'r') as f:
        N, M = map(int, f.readline().split())
        coors = np.array(list(map(float, f.readline().split()))).reshape((-1, 2))
        
    with open("output.txt", 'r') as f:
        idx, idy = map(int, f.readline().split())
        max_meteorites = int(f.readline())
        amounts = np.empty((N, M), dtype=int)
        for i in range(N):
            amounts[i, :] = np.array(list(map(int, f.readline().split())))
    
    plt.figure(figsize=(N, M))
    plt.scatter(coors[:, 0], coors[:, 1], c='r', s=4)
    plt.xticks(range(N+1))
    plt.yticks(range(M+1))
    plt.axis('equal')
    plt.grid()
    
    plt.plot([idx, idx+1, idx+1, idx, idx], [idy, idy, idy+1, idy+1, idy], 'k')
    for i in range(N):
        for j in range(M):
            plt.text(i+0.5, j+0.5, str(amounts[i, j]), fontsize=20)
    
    plt.savefig('meteorites.png', dpi=400)
    plt.show()