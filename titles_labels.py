import matplotlib.pyplot as plt

"""print("----titles and labels------")
x = [1, 2, 3]
y = [5, 7, 4]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.title('interesting Graph')
plt.show()

print("----titles and labels------")
x = [1, 2, 3]
y = [5, 7, 4]
x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label='first line')
plt.plot(x2, y2, label='second line')
plt.xlabel('plot number')
plt.ylabel('important var')

plt.title('interesting Graph')
plt.legend() 
plt.show()
"""
x = [1, 2, 3, 2, 1]
y = [4, 5, 7, 6, 4]
x2 = [1, 2, 2, 1, 1]
y2 = [7, 7, 4, 4, 7]
plt.plot(x, y, label='first line', linewidth=5)
plt.plot(x2, y2, label='second line', linewidth=5)
plt.xlabel("hitu")
plt.ylabel("rahul")
plt.title("brothers")
plt.legend()
plt.show()
