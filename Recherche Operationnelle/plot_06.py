import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0,13, 200)
c_1 = (81 - 3 * x_1) / 9
c_2 = (55 - 4. * x_1) / 5
c_3 = 20 - 2 * x_1


x1_points = [0, 0, 30/7, 7.5, 10]
x2_points = [0, 9, 53/7, 5, 0]
x_1_x_2_labels = ['(0,0)', '(0,9)', r'($\frac{30}{7}$,$\frac{53}{7}$)', '(7.5,5)', '(10,0)']


plt.plot(x_1, c_1, label=r'$3x_1 + 9x_2 \leq 81$', color='purple')
plt.plot(x_1, c_2, label=r'$4x_1 + 5x_2 \leq 55$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$2x_1 + x_2 \leq 20$', color='#708090')

c_feasible = np.minimum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, 0, c_feasible, where=(x_1 <= 90), color='lavender', alpha=0.5, label='L\'ensemble des solutions réalisables')
plt.scatter(x1_points, x2_points, color='#C43B7B', s=20, zorder=3)
plt.scatter(7.5, 5, color='#C43B7B', s=120, marker='*', label='Solution Optimale', zorder=3)

for i, txt in enumerate(x_1_x_2_labels):
    plt.annotate(txt,
                 (x1_points[i], x2_points[i]), 
                 textcoords="offset points",
                 xytext=(10, 5), 
                 ha='center', zorder=4) 

plt.xlim(0, 13)
plt.ylim(0, 13)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper right', facecolor='#FAFAFA')
plt.grid(True)
plt.show()