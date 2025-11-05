import numpy as np
import matplotlib.pyplot as plt

x_1 = np.linspace(0, 200, 400)
c_1 = (480 - x_1)/4
c_2 = (440 - 4*x_1)/2
c_3 = 150 - x_1

x1_points = [0, 90, 90, 70, 40, 0]
x2_points = [0, 0, 40, 80, 110, 120]
x_1_x_2_labels = ['(0,0)', '(90,0)', '(90,40)', '(70,80)', '(40,110)', '(0,120)']

plt.plot(x_1, c_1, label=r'$x_1 + 4x_2 \leq 480$', color='purple')
plt.plot(x_1, c_2, label=r'$4x_1 + 2x_2 \leq 440$', color='#BC8F8F')
plt.plot(x_1, c_3, label=r'$x_1 + x_2 \leq 150$', color='#708090')
plt.axvline(90, color='#BDB76B', label=r'$x_1 \leq 90$')

c_feasible = np.minimum.reduce([c_1, c_2, c_3])
plt.fill_between(x_1, 0, c_feasible, where=(x_1 <= 90), color='lavender', alpha=0.5, label='L\'ensemble des solutions réalisables')
plt.scatter(x1_points, x2_points, color='#C43B7B', s=20, zorder=3)
plt.scatter(40, 110, color='#C43B7B', s=120, marker='*', label='Solution Optimale', zorder=3)

for i, txt in enumerate(x_1_x_2_labels):
    plt.annotate(txt,
                 (x1_points[i], x2_points[i]), 
                 textcoords="offset points",
                 xytext=(10, 10), 
                 ha='center', zorder=4) 

plt.xlim(0, 200)
plt.ylim(0, 200)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper right', facecolor='#FAFAFA')
plt.grid(True)
plt.show()
