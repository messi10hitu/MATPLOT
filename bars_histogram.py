import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [1, 2, 3, 4, 5]
x2 = [4, 5, 2, 1, 6, 8]
y2 = [6, 4, 5, 2, 1, 8]

plt.bar(x, y, label='bars 1')
plt.bar(x2, y2, label='bars 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('BARS')
plt.legend()
plt.show()
'''
print("-----histograms-------")
population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54,
                   44, 43, 42, 48]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("histograms")
plt.legend()
plt.show()
'''
