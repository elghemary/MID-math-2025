import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 20, 400)
c_1 = (81 - 3 * x_1) / 9
c_2 = (55 - 4 * x_1) / 5
c_3 = 20 - 2 * x_1

plt.plot(x_1, c_1, label=r'$3x_1 + 9x_2 \leq 81$', color='purple')
plt.plot(x_1, c_2, label=r'$4x_1 + 5x_2 \leq 55$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$2x_1 + x_2 \leq 20$', color='#708090')


c_feasible = np.maximum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, c_feasible, 20, color='lavender', alpha=0.5, label="L'ensemble des solutions réalisables")

plt.scatter(0,0, color='#C43B7B', s=20, zorder=3)

plt.annotate(r'($\frac{126}{11}$,$\frac{23}{11}$)',
             (0,0),
             textcoords="offset points",
             xytext=(10, 10),
             ha='center', zorder=4)

plt.xlim(0, 20)
plt.ylim(0, 20)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper right', facecolor='#FAFAFA')
plt.grid(True)
plt.show()

