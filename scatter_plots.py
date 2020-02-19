import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 7, 4, 5, 8, 2, 1, 3]
plt.scatter(x, y, label='scattery', color='red', marker='*', s=100)  # s here is th marker size
plt.xlabel('x')
plt.ylabel('y')

plt.title('interesting Graph')
plt.legend()
plt.show()

