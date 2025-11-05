import numpy as np
import matplotlib.pyplot as plt

x_1 = np.linspace(0, 1000, 400)
c_1 = (9900 - 11 * x_1) / 9
c_2 = (8400 - 7 * x_1) / 12
c_3 = (9600 - 6 * x_1) / 16

x1_points = [0, 0, 480, 14400/23, 900]
x2_points = [0, 600, 420, 7700/23, 0]
x_1_x_2_labels = ['(0,0)', '(0,600)', '(480, 420)', r'($\frac{14400}{23}$, $\frac{7700}{23}$)', '(900,0)']

plt.plot(x_1, c_1, label=r'$11x_1 + 9x_2 \leq 9900$', color='purple')
plt.plot(x_1, c_2, label=r'$7x_1 + 12x_2 \leq 8400$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$6x_1 + 16x_2 \leq 9600$', color='#708090')

c_feasible = np.minimum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, 0, c_feasible, color='lavender', alpha=0.5, label='L\'ensemble des solutions réalisables')
plt.scatter(x1_points, x2_points, color='#C43B7B', s=20, zorder=3)
plt.scatter(14400/23, 7700/23, color='#C43B7B', s=120, marker='*', label='Solution Optimale', zorder=3)

for i, txt in enumerate(x_1_x_2_labels):
    plt.annotate(txt,
                 (x1_points[i], x2_points[i]), 
                 textcoords="offset points",
                 xytext=(30, 10), 
                 ha='center', zorder=4) 

plt.xlim(0, 1000)
plt.ylim(0, 900)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper right', facecolor='#FAFAFA')
plt.grid(True)
plt.show()
