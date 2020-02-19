import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

# part1 ==> Load data using built in CSV
'''
x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label="loaded drom file!")

# part2 ==> Load data using numpy
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x, y, label="loaded from file!")
plt.xlabel('plot number')
plt.ylabel('important var')

plt.title('Data Graph')
plt.legend()
plt.show()
'''
