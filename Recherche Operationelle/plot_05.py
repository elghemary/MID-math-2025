import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 10, 200)
c_1 = (18 - x_1) / 3
c_2 = 8 - x_1 
c_3 = 14 - 2 * x_1


x1_points = [0, 0, 3, 6, 7]
x2_points = [0, 6, 5, 2, 0]
x_1_x_2_labels = ['(0,0)', '(0,6)', '(3,5)', '(6,2)', '(7,0)']


plt.plot(x_1, c_1, label=r'$x_1 + 3x_2 \leq 18$', color='purple')
plt.plot(x_1, c_2, label=r'$x_1 + 8x_2 \leq 8$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$2x_1 + x_2 \leq 14$', color='#708090')

c_feasible = np.minimum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, 0, c_feasible, where=(x_1 <= 90), color='lavender', alpha=0.5, label='L\'ensemble des solutions réalisables')
plt.scatter(x1_points, x2_points, color='#C43B7B', s=20, zorder=3)
plt.scatter(3, 5, color='#C43B7B', s=120, marker='*', label='Solution Optimale', zorder=3)

for i, txt in enumerate(x_1_x_2_labels):
    plt.annotate(txt,
                 (x1_points[i], x2_points[i]), 
                 textcoords="offset points",
                 xytext=(10, 10), 
                 ha='center', zorder=4) 

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper right', facecolor='#FAFAFA')
plt.grid(True)
plt.show()