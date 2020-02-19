import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 7, 5, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']
plt.pie(slices,
        labels=activities,  # used to add labels and here we use labels instead of label
        colors=cols,  # here we used colors instead of color
        startangle=90,
        explode=(0, 0.1, 0.1, 0),  # it will break th piechaart or seperate the pies
        autopct='%1.1f%%'  # Autopercentage => it gives the % and the formula is (%1.1f%%)
        )
plt.title('pie chart')

plt.show()
