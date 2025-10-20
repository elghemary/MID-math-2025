import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 20, 400)
c_1 = (18 - x_1) / 3
c_2 = 8 - x_1 
c_3 = 14 - 2 * x_1

plt.plot(x_1, c_1, label=r'$x_1 + 3x_2 \leq 18$', color='purple')
plt.plot(x_1, c_2, label=r'$x_1 + 8x_2 \leq 8$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$2x_1 + x_2 \leq 14$', color='#708090')


c_feasible = np.maximum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, c_feasible, 20, color='lavender', alpha=0.5, label="L'ensemble des solutions réalisables")

plt.scatter(0,0, color='#C43B7B', s=20, zorder=3)

plt.annotate(r'($\frac{126}{11}$,$\frac{23}{11}$)',
             (126/11, 23/11),
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

