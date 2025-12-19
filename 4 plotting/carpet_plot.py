import numpy as np
from matplotlib import pyplot as plt

def carpet(n):
    # Recursive Sierpiński carpet
    if n == 1:
        return [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    else:
        ref = carpet(n - 1)
        row0 = carpet(n - 1)
        row1 = carpet(n - 1)
        row2 = carpet(n - 1)

        row_of_zeros = [0] * len(ref)
        for i in range(len(ref)):
            row0[i].extend(ref[i])
            row0[i].extend(ref[i])
            row1[i].extend(row_of_zeros)
            row1[i].extend(ref[i])
            row2[i].extend(ref[i])
            row2[i].extend(ref[i])
        row0.extend(row1)
        row0.extend(row2)

        return row0


n = int(input())
# Convert to numpy and plot
arr = np.array(carpet(n))
plt.imshow(arr, cmap='Greys')
plt.savefig("carpet.png", dpi=200)