from matplotlib import pyplot as plt

# plot data from file
file = open('data.txt', 'r')

X = []
Y = []

for line in file:
    X.append(int(line.strip().split()[0]))
    Y.append(int(line.strip().split()[1]))

plt.plot(X, Y)
plt.grid()
plt.show()

file.close()