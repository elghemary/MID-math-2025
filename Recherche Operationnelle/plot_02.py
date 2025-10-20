import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 30, 100)
c_1 = 12 - 2 * x_1
c_2 = (74 - 5 * x_1) / 8
c_3 = (24 - x_1) / 6

x1_points = [0, 2, 126/11, 24]
x2_points = [12, 8, 23/11, 0]
x_1_x_2_labels = ['(0,12)', '(2,8)', r'($\frac{126}{11}$,$\frac{23}{11}$)', '(24,12)']

plt.plot(x_1, c_1, label=r'$2x_1 + 2x_2 \geq 12$', color='purple')
plt.plot(x_1, c_2, label=r'$5x_1 + 8x_2 \geq 74$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$x_1 + 6x_2 \geq 24$', color='#708090')


c_feasible = np.maximum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, c_feasible, 20, color='lavender', alpha=0.5, label="L'ensemble des solutions réalisables")

plt.scatter(x1_points, x2_points, color='#C43B7B', s=20, zorder=3)
plt.scatter(2, 8, color='#C43B7B', s=120, marker='*', label='Solution Optimale', zorder=3)

for i, txt in enumerate(x_1_x_2_labels):
    plt.annotate(txt,
                 (x1_points[i], x2_points[i]), 
                 textcoords="offset points",
                 xytext=(10, 10), 
                 ha='center', zorder=4) 

plt.xlim(0, 30)
plt.ylim(0, 15)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper right', facecolor='#FAFAFA')
plt.grid(True)
plt.show()

