import numpy as np
from matplotlib import pyplot as plt
g = 1.4 #можно варьировать коэффициент
f1 = lambda x: 900. / x
f2 = lambda x: 900. * (50. ** (g - 1.)) / (x ** g)
f3 = lambda x: ((30. ** (g + 1.)) / (46. ** (g - 1.))) / x
f4 = lambda x: (30. ** (g + 1.)) / (x ** g)
n = 101
xx = np.linspace(30, 80, n)
# Find index of minimal value
i1 = 0
i2 = np.argmin(np.abs(f1(xx) - f2(xx)))
i3 = np.argmin(np.abs(f2(xx) - f3(xx)))
i4 = np.argmin(np.abs(f3(xx) - f4(xx)))
x1 = 30.0
x2 = xx[i2]
x3 = xx[i3]
x4 = xx[i4]
fig, ax = plt.subplots(figsize=(5, 3))
plt.xticks(range(30, 90, 10))
plt.yticks(range(10, 40, 10))
xx1 = xx[i1:i2+1]
ax.plot(xx1, f1(xx1), 'b-', label='1-2 isotermal')
xx2 = xx[i2:i3+1]
ax.plot(xx2, f2(xx2), 'g-', label='2-3 adiabatic')
xx3 = xx[i4:i3+1]
ax.plot(xx3, f3(xx3), 'y-', label='3-4 isotermal')
xx4 = xx[i1:i4+1]
ax.plot(xx4, f4(xx4), 'r-', label='4-1 adiabatic')
ax.plot(30., 30., 'ko')
ax.plot(x2, f1(x2), 'ko')
ax.plot(x3, f2(x3), 'ko')
ax.plot(x4, f3(x4), 'ko')
ax.set(xlabel='$\mathit{V}$',
       title='P-V diagram of Carnot cycle')
ax.set_ylabel('$\mathit{p}$', rotation=0, labelpad=10)
ax.set_xlim(25., 85.)
ax.set_ylim(5., 35.)
plt.text(31., 30., '1')
plt.text(x2+1., f1(x2), '2')
plt.text(x3+1., f2(x3), '3')
plt.text(x4+1., f4(x4), '4')
plt.legend()
ax.grid()
plt.savefig('intersection.png', dpi = 600, format = 'png')
plt.show()
#plt.close()